from rest_framework import serializers
from .models import DepositProduct, DepositOption, SavingProduct, SavingOption, DepositProductList, SavingProductList


# 예금상품 rawdata
class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'


# 예금상품옵션 rawdata
class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields = ('depositproduct',)


# 적금상품 rawdata
class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'


# 적금상품옵션 rawdata
class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ('savingproduct',)


# 예금상품 리스트
class DepositProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProductList
        fields = '__all__'
        read_only_fields = ('savingproduct', 'like_users')


# 적금상품 리스트
class SavingProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProductList
        fields = '__all__'
        read_only_fields = ('like_users',)





