import requests
import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from accounts.models import User, CustomPortfolio
from .models import DepositProduct, DepositOption, SavingProduct, SavingOption, DepositProductList, SavingProductList
from .serializers import DepositProductSerializer, DepositOptionSerializer, SavingProductSerializer, SavingOptionSerializer, DepositProductListSerializer, SavingProductListSerializer
from accounts.models import User
from django.core.mail import send_mail

import json
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

from django.conf import settings


# 정기예금 실행 시 작동
# 금융감독원의 "정기예금" API 로 부터 자료를 수신받아
# 데이터베이스에 저장하고,
# 저장된 데이터베이스를 JSON 형태로 반환
@api_view(['GET'])
def deposit_list(request):
    # API 키
    API_KEY = settings.FINANCE_API_KEY

    # 금융감독원 정기예금 JSON 요청 API
    URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    
    # JSON 데이터 불러오기
    response = requests.get(URL).json()

    # 예금상품을 DepositProduct 에 저장하기
    for prdt in response.get('result').get('baseList'):

        # 중복값 검사하기
        is_duplicated = False
        for record in DepositProduct.objects.all():
            if record.fin_prdt_cd == prdt.get('fin_prdt_cd'):
                is_duplicated = True
                break
        if is_duplicated:
            continue

        # DB 레코드에 저장할 각 인스턴스 생성
        prdt_data = {
            'dcls_month': prdt.get('dcls_month'),  
            'fin_co_no': prdt.get('fin_co_no'),               
            'fin_prdt_cd': prdt.get('fin_prdt_cd'),
            'kor_co_nm': prdt.get('kor_co_nm'),
            'fin_prdt_nm': prdt.get('fin_prdt_nm'),
            'join_way': prdt.get('join_way'),
            'mtrt_int': prdt.get('mtrt_int'),
            'spcl_cnd': prdt.get('spcl_cnd'),
            'join_deny': prdt.get('join_deny'),
            'join_member': prdt.get('join_member'),
            'etc_note': prdt.get('etc_note'),
            'max_limit': prdt.get('max_limit'),
            'dcls_strt_day': prdt.get('dcls_strt_day'),
            'dcls_end_day': prdt.get('dcls_end_day'),
            'fin_co_subm_day': prdt.get('fin_co_subm_day'),
        }

        serializer = DepositProductSerializer(data=prdt_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 상품옵션을 DepositOption 에 저장하기
    for opt in response.get('result').get('optionList'):
        
        # 해당 옵션이 속한 상품의 코드
        prdt_cd = opt.get('fin_prdt_cd')

        # 해당 상품 객체 불러오기
        prdt = DepositProduct.objects.get(fin_prdt_cd=prdt_cd)
        
        # 중복값 검사하기
        is_duplicated = False
        for record in DepositOption.objects.all():
            if record.fin_prdt_cd == prdt_cd and record.save_trm == opt.get('save_trm'):
                is_duplicated = True
                break
        if is_duplicated:
            continue

        # DB 레코드에 저장할 각 인스턴스 생성
        opt_data = {
            'dcls_month': opt.get('dcls_month'),
            'fin_co_no': opt.get('fin_co_no'),
            'fin_prdt_cd': opt.get('fin_prdt_cd'),
            'intr_rate_type': opt.get('intr_rate_type'),
            'intr_rate_type_nm': opt.get('intr_rate_type_nm'),
            'save_trm': opt.get('save_trm'),
            'intr_rate': opt.get('intr_rate'),
            'intr_rate2': opt.get('intr_rate2'),
        }

        serializer = DepositOptionSerializer(data=opt_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(depositproduct=prdt)


    # 상품별 이자옵션 기재된 새로운 DB 저장
    # DB에 저장된 각 상품에 대하여
    for product in DepositProduct.objects.all():

        # 중복값 검사하기
        is_duplicated = False
        for record in DepositProductList.objects.all():
            if record.fin_prdt_cd == product.fin_prdt_cd:
                is_duplicated = True
                break
        if is_duplicated:
            continue


        # DB에 저장된 해당 상품의 모든 옵션들 불러오기
        options = product.depositoption_set.all()

        # 6개월, 12개월, 24개월, 36개월 이자 정보를 저장할 인스턴스
        rate_6 = None
        rate_6_max = None
        rate_12 = None
        rate_12_max = None
        rate_24 = None
        rate_24_max = None
        rate_36 = None
        rate_36_max = None

        # 기간별로 이자 정보 등록하기
        for option in options:
            period = option.save_trm
            rate1 = option.intr_rate
            rate2 = option.intr_rate2

            if period == '6':
                rate_6 = rate1
                rate_6_max = rate2
            elif period == '12':
                rate_12 = rate1
                rate_12_max = rate2
            elif period == '24':
                rate_24 = rate1
                rate_24_max = rate2
            elif period == '36':
                rate_36 = rate1
                rate_36_max = rate2


        # DB 에 넣을 data 취합하기
        prdt_with_rate = {
            'dcls_month': product.dcls_month,                  
            'fin_prdt_cd': product.fin_prdt_cd,
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'rate_6': rate_6,
            'rate_6_max': rate_6_max,
            'rate_12': rate_12,
            'rate_12_max': rate_12_max,
            'rate_24': rate_24,
            'rate_24_max': rate_24_max,
            'rate_36': rate_36,
            'rate_36_max': rate_36_max,
        }

        serializer = DepositProductListSerializer(data=prdt_with_rate)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 프론트로 리스트 데이터 전송하기
    products = get_list_or_404(DepositProductList)
    serializer = DepositProductListSerializer(products, many=True)

    return Response(serializer.data)


# 적금 실행 시 작동
# 금융감독원의 "적금" API 로 부터 자료를 수신받아
# 데이터베이스에 저장하고,
# 저장된 데이터베이스를 JSON 형태로 반환
@api_view(['GET'])
def saving_list(request):
    # API 키
    API_KEY = settings.FINANCE_API_KEY

    # 금융감독원 적금 JSON 요청 API
    URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    
    # JSON 데이터 불러오기
    response = requests.get(URL).json()

    # 적금상품을 SavingProduct 에 저장하기
    for prdt in response.get('result').get('baseList'):

        # 중복값 검사하기
        is_duplicated = False
        for record in SavingProduct.objects.all():
            if record.fin_prdt_cd == prdt.get('fin_prdt_cd'):
                is_duplicated = True
                break
        if is_duplicated:
            continue

        # DB 레코드에 저장할 각 인스턴스 생성
        prdt_data = {
            'dcls_month': prdt.get('dcls_month'),  
            'fin_co_no': prdt.get('fin_co_no'),               
            'fin_prdt_cd': prdt.get('fin_prdt_cd'),
            'kor_co_nm': prdt.get('kor_co_nm'),
            'fin_prdt_nm': prdt.get('fin_prdt_nm'),
            'join_way': prdt.get('join_way'),
            'mtrt_int': prdt.get('mtrt_int'),
            'spcl_cnd': prdt.get('spcl_cnd'),
            'join_deny': prdt.get('join_deny'),
            'join_member': prdt.get('join_member'),
            'etc_note': prdt.get('etc_note'),
            'max_limit': prdt.get('max_limit'),
            'dcls_strt_day': prdt.get('dcls_strt_day'),
            'dcls_end_day': prdt.get('dcls_end_day'),
            'fin_co_subm_day': prdt.get('fin_co_subm_day'),
        }

        serializer = SavingProductSerializer(data=prdt_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 상품옵션을 SavingOption 에 저장하기
    for opt in response.get('result').get('optionList'):
        
        # 해당 옵션이 속한 상품의 코드
        prdt_cd = opt.get('fin_prdt_cd')

        # 해당 상품 객체 불러오기
        prdt = SavingProduct.objects.get(fin_prdt_cd=prdt_cd)
        
        # 중복값 검사하기
        is_duplicated = False
        for record in SavingOption.objects.all():
            if record.fin_prdt_cd == prdt_cd and record.save_trm == opt.get('save_trm'):
                is_duplicated = True
                break
        if is_duplicated:
            continue

        # DB 레코드에 저장할 각 인스턴스 생성
        opt_data = {
            'dcls_month': opt.get('dcls_month'),
            'fin_co_no': opt.get('fin_co_no'),
            'fin_prdt_cd': opt.get('fin_prdt_cd'),
            'intr_rate_type': opt.get('intr_rate_type'),
            'intr_rate_type_nm': opt.get('intr_rate_type_nm'),
            'rsrv_type': opt.get('rsrv_type'),
            'rsrv_type_nm': opt.get('rsrv_type_nm'),
            'save_trm': opt.get('save_trm'),
            'intr_rate': opt.get('intr_rate'),
            'intr_rate2': opt.get('intr_rate2'),
        }

        serializer = SavingOptionSerializer(data=opt_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(savingproduct=prdt)


    # 상품별 이자옵션 기재된 새로운 DB 저장
    # DB에 저장된 각 상품에 대하여
    for product in SavingProduct.objects.all():

        # 중복값 검사하기
        is_duplicated = False
        for record in SavingProductList.objects.all():
            if record.fin_prdt_cd == product.fin_prdt_cd:
                is_duplicated = True
                break
        if is_duplicated:
            continue


        # DB에 저장된 해당 상품의 모든 옵션들 불러오기
        options = product.savingoption_set.all()

        # 6개월, 12개월, 24개월, 36개월 이자 정보를 저장할 인스턴스
        rate_6 = None
        rate_6_max = None
        rate_12 = None
        rate_12_max = None
        rate_24 = None
        rate_24_max = None
        rate_36 = None
        rate_36_max = None

        # 기간별로 이자 정보 등록하기
        for option in options:
            period = option.save_trm
            rate1 = option.intr_rate
            rate2 = option.intr_rate2

            if period == '6':
                rate_6 = rate1
                rate_6_max = rate2
            elif period == '12':
                rate_12 = rate1
                rate_12_max = rate2
            elif period == '24':
                rate_24 = rate1
                rate_24_max = rate2
            elif period == '36':
                rate_36 = rate1
                rate_36_max = rate2


        # DB 에 넣을 data 취합하기
        prdt_with_rate = {
            'dcls_month': product.dcls_month,                  
            'fin_prdt_cd': product.fin_prdt_cd,
            'kor_co_nm': product.kor_co_nm,
            'fin_prdt_nm': product.fin_prdt_nm,
            'rate_6': rate_6,
            'rate_6_max': rate_6_max,
            'rate_12': rate_12,
            'rate_12_max': rate_12_max,
            'rate_24': rate_24,
            'rate_24_max': rate_24_max,
            'rate_36': rate_36,
            'rate_36_max': rate_36_max,
        }

        serializer = SavingProductListSerializer(data=prdt_with_rate)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    # 프론트로 리스트 데이터 전송하기
    products = get_list_or_404(SavingProductList)
    serializer = SavingProductListSerializer(products, many=True)
    return Response(serializer.data)


# 예금 상품 상세 데이터 불러오는 view
# POST 요청일 경우, 해당 상세 상품을 로그인한 유저 계정의 financial_products 필드에 추가
@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def deposit_detail(request, fin_prdt_cd):
    # 상품 상세 정보 보기
    if request.method == 'GET':
        product = get_object_or_404(DepositProduct, fin_prdt_cd=fin_prdt_cd)
        serializer = DepositProductSerializer(product)
        return Response(serializer.data)
    
    # 해당 상품 가입하기
    elif request.method == 'POST':
        # 유저정보 불러오기
        deposit = DepositProductList.objects.get(fin_prdt_cd=fin_prdt_cd)
        if request.user in deposit.like_users.all():
            return Response(status=status.HTTP_409_CONFLICT)
            
        else:
            deposit.like_users.add(request.user)
            return Response(status=status.HTTP_200_OK)


    # 해당 상품 금리 수정하기
    elif request.method == 'PUT':
        # 전달받은 신규 금리
        new_rate = request.data.get('rate')     # 신규 금리
        rateType = request.data.get('rateType') # 금리 타입
        
        option = DepositOption.objects.get(fin_prdt_cd=fin_prdt_cd, save_trm=rateType)
        
        list_new_rate = DepositProductList.objects.get(fin_prdt_cd=fin_prdt_cd)

        serializer1 = DepositOptionSerializer(option, data={'intr_rate': new_rate}, partial=True)
        serializer2 = DepositProductListSerializer(list_new_rate, data={f'rate_{rateType}': new_rate}, partial=True)

        if serializer1.is_valid() and serializer2.is_valid():
            serializer1.save()
            serializer2.save()
            return Response({"message": "true"})
        else:
            return Response({"message": "false"})



# 적금 상품 상세 데이터 불러오는 view
@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def saving_detail(request, fin_prdt_cd):
    if request.method == 'GET':
        product = get_object_or_404(SavingProduct, fin_prdt_cd=fin_prdt_cd)
        serializer = SavingProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # 유저정보 불러오기
        saving = SavingProductList.objects.get(fin_prdt_cd=fin_prdt_cd)
        if request.user in saving.like_users.all():
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            saving.like_users.add(request.user)
            return Response(status=status.HTTP_200_OK)

    # 해당 상품 금리 수정하기
    elif request.method == 'PUT':
        # 전달받은 신규 금리
        new_rate = request.data.get('rate')     # 신규 금리
        rateType = request.data.get('rateType') # 금리 타입


        option = SavingOption.objects.get(fin_prdt_cd=fin_prdt_cd, save_trm=rateType)
        

        list_new_rate = SavingProductList.objects.get(fin_prdt_cd=fin_prdt_cd)

        serializer1 = SavingOptionSerializer(option, data={'intr_rate': new_rate}, partial=True)
        serializer2 = SavingProductListSerializer(list_new_rate, data={f'rate_{rateType}': new_rate}, partial=True)

        if serializer1.is_valid() and serializer2.is_valid():
            serializer1.save()
            serializer2.save()
            return Response({"message": "true"})
        else:
            return Response({"message": "false"})



# 금리 변동 시 이메일 발송
@api_view(['GET'])
def send_email_on_change(request):
    # 상품코드, 기존금리, 변경금리 받아온 것
    prdt_code = request.GET.get('prdtCode')
    old_rate = request.GET.get('oldRate')
    new_rate = request.GET.get('newRate')
    period = request.GET.get('period')


    try:
        product = DepositProductList.objects.get(fin_prdt_cd=prdt_code)
    except:
        product = SavingProductList.objects.get(fin_prdt_cd=prdt_code)
    

    # 해당 상품명
    prdt_name = product.fin_prdt_nm


    # 해당 상품 가입한 유저들 이메일 수집하기
    to = []     # 이메일 목록

    for user in product.like_users.all():
        to.append(user.email)


    # 이메일 내용
    title = '[BankSailor] 가입하신 상품의 금리정보가 변동되어 안내드립니다'
    content = f'안녕하세요 고객님, 가입하신 {prdt_name} 상품의 금리정보가 변동되어 안내드립니다.\n\n금리옵션: {period}개월\n변동 전 금리: {old_rate}%\n변동 후 금리: {new_rate}%'
    
    # 이메일 보내기
    send_mail(
        title,
        content,
        settings.EMAIL_ADDRESS,
        to,
    )


    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def recommend(request):
    if request.method == 'POST':

        USERPK = request.user.pk

        # 1. age, salary, money 비슷한 유저들 뽑고 그 유저들은 뭐 쓰는지 보여주기
        data = User.objects.all()
        data_list = list(data.values('id', 'money', 'age', 'salary'))
        print(data_list)
        df = pd.DataFrame.from_records(data_list)
        # # index를 id로 지정
        df.set_index('id', inplace=True)
        # # 사용할 특성 선택
        features = ['age', 'money', 'salary']
        # # 특성 스케일링
        scaler = StandardScaler()
        df[features] = scaler.fit_transform(df[features]) 
        df[features] = df[features].fillna(df[features].mean())

        # # Find the features of the current user
        user_data = df.loc[USERPK].values.reshape(1, -1)

        # # KNN 모델 생성
        knn_model = NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
        knn_model.fit(df[features])

        distances, indices = knn_model.kneighbors(user_data)

        # # 가장 가까운 이웃의 인덱스를 이용하여 pk(id) 값을 가져오기
        closest_neighbors_ids = df.index[indices[0]]
        # print(indices)
        # # 결과 로깅
        recommend_deposit = []
        recommend_saving = []
        now_user = request.user
        now_user_liked_deposits = now_user.like_deposit.all()
        now_user_liked_savings = now_user.like_saving.all()

        for id in closest_neighbors_ids:
            if id != USERPK:
                other_user = User.objects.get(pk=id)
                other_user_liked_deposits = other_user.like_deposit.all()
                other_user_liked_savings = other_user.like_saving.all()

                for d in other_user_liked_deposits:
                    if d not in now_user_liked_deposits and len(recommend_deposit) < 3:
                        recommend_deposit.append(d)

                for s in other_user_liked_savings:
                    if s not in now_user_liked_savings and len(recommend_saving) < 3:
                        recommend_saving.append(s)

        deposit_serializer = DepositProductListSerializer(recommend_deposit, many=True)
        saving_serializer = SavingProductListSerializer(recommend_saving, many=True)

        serialized_data = {
            'deposits': deposit_serializer.data,
            'savings': saving_serializer.data
        }
        return Response(serialized_data)




















@api_view(['POST'])
def iwillrecommendyou(request):
    # 현재 로그인된 유저 정보 가져오기
    mydata = request.data
    
    with open('./accounts/fixtures/user_saving.json', encoding='utf-8') as file:
        datas = json.load(file)

    # fields 안에 내가 원하는 정보가 있기 때문에 뽑아오기
    users_info = []
    for user_data in datas:
        user_fields = user_data.get('fields', {})
        user_info = {
            'pk': user_data.get('pk', 0),
            'fin_prdt_cd': user_fields.get('financial_products', 0),
            'age': user_fields.get('age', 0),
            'money': user_fields.get('money', 0),
            'salary': user_fields.get('salary', 0),
            'saving_style':user_fields.get('saving_style', 0)
        }
        users_info.append(user_info)
    
    user_df = pd.DataFrame(users_info)
    # 상품 미가입된 유저 정보 제외
    new_df = user_df.drop(index=user_df[user_df['fin_prdt_cd']==''].index)
    
    # 새로운 행을 저장할 리스트와 삭제할 행의 인덱스 리스트 초기화
    new_rows = []
    rows_to_delete = []

    # 새로운 행 생성하고 삭제할 행 인덱스 기록
    for index, row in new_df.iterrows():
        codes = row['fin_prdt_cd'].split(',')
        if len(codes) > 1:
            rows_to_delete.append(index)
            for code in codes[1:]:
                new_row = row.copy()
                new_row['fin_prdt_cd'] = code.strip()
                new_rows.append(new_row)

    # 새로운 행들을 데이터프레임에 추가
    if new_rows:
        new_df = new_df.drop(rows_to_delete)  # 삭제할 행 제거
        new_df = pd.concat([new_df, pd.DataFrame(new_rows)], ignore_index=True) 

    # 조건에 따라 점수 매기기
    def calculate_rate(row):
        score = 0

        # 조건 1: 나이 일치 여부
        if str(mydata['age'])[0] == str(row['age'])[0]:
            score += 1
        else:
            score -= 1

        # 조건 2: saving_style 일치 여부
        if mydata['saving_style'] == row['saving_style']:
            score += 2

        # 조건 3: salary 자릿수 일치 여부
        if len(str(mydata['salary'])) == len(str(row['salary'])):
            score += 1

        # 조건 4: money 자릿수 일치 여부
        if len(str(mydata['money'])) == len(str(row['money'])):
            score += 1

        return score

    # 점수 계산하여 새로운 열 추가
    new_df['score'] = new_df.apply(calculate_rate, axis=1)
    score_table = new_df.pivot_table('score', index='pk', columns= 'fin_prdt_cd').fillna(0)
    transpose_table = score_table.values.T
    
    # SVD.fit_transform을 통해 변환하게 되면 8380개의 영화 데이터가 12개의 어떤 요소의 값을 가지게 됩니다.
    SVD = TruncatedSVD(n_components=12)
    # 결측치를 제거하고 데이터끼리 피어슨 상관계수를 통해 구해줍니다
    matrix = SVD.fit_transform(transpose_table)

    corr = np.corrcoef(matrix)
    
    # 상관계수를 이용하여 '내가 가입한 상품'과 관련해 상관계수가 높은 상품을 뽑아주면 됩니다.
    prd_name = score_table.columns
    prd_name_list = list(prd_name)
    coffey_hands = prd_name_list.index('00266451')
    corr_coffey_hands = corr[coffey_hands]
    result_list = list(prd_name[(corr_coffey_hands >= 0.1)])[:11]
    print(result_list)
    
    # for result in result_list:
    #     recommend_list = SavingProductList.objects.filter(fin_prdt_cd=result)
    recommend_list = SavingProductList.objects.filter(fin_prdt_cd__in=result_list)
    print(recommend_list)
        
    serializer = SavingProductListSerializer(recommend_list, many=True)        
    print(serializer.data)
    return Response(serializer.data)

    
