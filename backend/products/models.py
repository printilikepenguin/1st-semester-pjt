from django.db import models
from accounts.models import User



# 정기예금 상품 테이블
class DepositProduct(models.Model):
    dcls_month = models.CharField(max_length=50)   
    fin_co_no = models.CharField(max_length=50)                 
    fin_prdt_cd = models.CharField(max_length=50, unique=True)
    kor_co_nm = models.CharField(max_length=50)
    fin_prdt_nm = models.CharField(max_length=100)
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField(blank=True, null=True)
    dcls_strt_day = models.CharField(max_length=50)
    dcls_end_day = models.CharField(max_length=50, blank=True, null=True)
    fin_co_subm_day = models.CharField(max_length=50)


# 정기예금 옵션 테이블
class DepositOption(models.Model):
    # 상품참조할 외래키 설정
    depositproduct = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    dcls_month = models.CharField(max_length=50)
    fin_co_no = models.CharField(max_length=50)
    fin_prdt_cd = models.CharField(max_length=50)
    intr_rate_type = models.CharField(max_length=50)
    intr_rate_type_nm = models.CharField(max_length=50)
    save_trm = models.CharField(max_length=50)
    intr_rate = models.FloatField(blank=True, null=True)
    intr_rate2 = models.FloatField(blank=True, null=True)


# 정기예금 상품 리스트화 모델
class DepositProductList(models.Model):
    # 유저랑 연결
    like_users = models.ManyToManyField(User, related_name='like_deposit')
    dcls_month = models.CharField(max_length=50)                  
    fin_prdt_cd = models.CharField(max_length=50)
    kor_co_nm = models.CharField(max_length=50)
    fin_prdt_nm = models.CharField(max_length=100)
    rate_6 = models.FloatField(blank=True, null=True)
    rate_6_max = models.FloatField(blank=True, null=True)
    rate_12 = models.FloatField(blank=True, null=True)
    rate_12_max = models.FloatField(blank=True, null=True)
    rate_24 = models.FloatField(blank=True, null=True)
    rate_24_max = models.FloatField(blank=True, null=True)
    rate_36 = models.FloatField(blank=True, null=True)
    rate_36_max = models.FloatField(blank=True, null=True)


# 적금 상품 테이블
class SavingProduct(models.Model):
    dcls_month = models.CharField(max_length=50)   
    fin_co_no = models.CharField(max_length=50)                 
    fin_prdt_cd = models.CharField(max_length=50, unique=True)
    kor_co_nm = models.CharField(max_length=50)
    fin_prdt_nm = models.CharField(max_length=100)
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField(blank=True, null=True)
    dcls_strt_day = models.CharField(max_length=50)
    dcls_end_day = models.CharField(max_length=50, blank=True, null=True)
    fin_co_subm_day = models.CharField(max_length=50)


# 적금 옵션 테이블
class SavingOption(models.Model):
    # 상품참조할 외래키 설정
    savingproduct = models.ForeignKey(SavingProduct, on_delete=models.CASCADE)
    
    dcls_month = models.CharField(max_length=50)
    fin_co_no = models.CharField(max_length=50)
    fin_prdt_cd = models.CharField(max_length=50)
    intr_rate_type = models.CharField(max_length=50)
    intr_rate_type_nm = models.CharField(max_length=50)
    rsrv_type = models.CharField(max_length=50)
    rsrv_type_nm = models.CharField(max_length=50)
    save_trm = models.CharField(max_length=50)
    intr_rate = models.FloatField(blank=True, null=True)
    intr_rate2 = models.FloatField(blank=True, null=True)


# 적금 상품 리스트화 모델
class SavingProductList(models.Model):
    # 유저랑 연결
    like_users = models.ManyToManyField(User, related_name='like_saving')
    dcls_month = models.CharField(max_length=50)                  
    fin_prdt_cd = models.CharField(max_length=50)
    kor_co_nm = models.CharField(max_length=50)
    fin_prdt_nm = models.CharField(max_length=100)
    rate_6 = models.FloatField(blank=True, null=True)
    rate_6_max = models.FloatField(blank=True, null=True)
    rate_12 = models.FloatField(blank=True, null=True)
    rate_12_max = models.FloatField(blank=True, null=True)
    rate_24 = models.FloatField(blank=True, null=True)
    rate_24_max = models.FloatField(blank=True, null=True)
    rate_36 = models.FloatField(blank=True, null=True)
    rate_36_max = models.FloatField(blank=True, null=True)

    