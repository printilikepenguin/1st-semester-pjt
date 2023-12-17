from django.urls import path
from . import views

app_name = 'exchange'
urlpatterns = [
    path('currency/<str:fromCountry>/<int:price>/<str:st_date>/<str:howlong>/', views.exchange),
    # path('exchange/diff/<str:st_date>/', views.get_exchange_diff),
]

