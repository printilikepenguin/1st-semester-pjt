from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from .models import User, CustomPortfolio
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from products.models import DepositProductList, SavingProductList

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    # financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'email': self.validated_data.get('email', ''),
            'age': self.validated_data.get('age', ''),
            'money': self.validated_data.get('money', ''),
            'salary': self.validated_data.get('salary', ''),
            # 'financial_products': self.validated_data.get('financial_products', ''),
        }


    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProductList
        fields = '__all__' 

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProductList
        fields = '__all__' 



# getuserinfo하면 deposit까지 한번에 나오게 하려고!
class CustomUserSerializer(serializers.ModelSerializer):
    like_deposit = DepositSerializer(many=True, read_only=True)
    like_saving = SavingSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'  


class CustomPortfolioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = CustomPortfolio
        fields = '__all__'