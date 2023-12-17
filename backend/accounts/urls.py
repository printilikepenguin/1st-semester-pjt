from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('duplicateID/', views.duplicateID),
    path('get_portfolioData/<int:portfolio_pk>', views.get_portfolioData),
    path('input_portfolioData/', views.input_portfolioData),
    path('check_password/', views.check_password),
    path('update/', views.updateinfo)
]

