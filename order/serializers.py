from rest_framework import serializers
from .models import OrderModel, ProductInOrderModel



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'.split()


class ProductInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInOrderModel
        fields = '__all__'.split()