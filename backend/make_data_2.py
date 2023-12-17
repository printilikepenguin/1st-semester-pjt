import random
import requests

# deposit 38개
# saving 50개
# user 10000명

dict_keys = ['saving_style', 'favorite_bank', 'user_id']

# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()
banklist = [
  "KEB하나은행",
  "SC제일은행",
  "국민은행",
  "신한은행",
  "외환은행",
  "우리은행",
  "한국시티은행",
  "지방은행",
  "경남은행",
  "광주은행",
  "대구은행",
  "부산은행",
  "전북은행",
  "제주은행",
  "특수은행",
  "기업은행",
  "농협",
  "수협",
  "한국산업은행",
  "한국수출입은행",
]

N = 11
# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = '../backend/accounts/fixtures/user_data_2.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    for i in range(N):
        file["model"] = "accounts.customportfolio"
        file["pk"] = i+1
        file["fields"] = {
            # 'depositproductlist' : [random.randrange(1,38)],
            'saving_style': random.choice(['알뜰형', '도전형', '성실형']),
            'favorite_bank': random.choice(banklist),
            'user_id': i+1
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')