from django.urls import path
from . import views

urlpatterns = [
    # 정기예금 url
    path('deposit/', views.deposit_list),
    # 정기예금 상세정보 url
    path('deposit/<str:fin_prdt_cd>/', views.deposit_detail),
    # 적금 url
    path('saving/', views.saving_list),
    # 적금 상세정보 url
    path('saving/<str:fin_prdt_cd>/', views.saving_detail),
    # 금리 변동시 이메일 발송
    path('email/', views.send_email_on_change),
    # 금리 변동시 이메일 발송
    path('recommend/', views.recommend),
    # 유형별 맞춤상품
    path('iwillrecommendyou/', views.iwillrecommendyou),
]