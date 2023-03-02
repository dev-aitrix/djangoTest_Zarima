from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer, ProductInOrderSerializer
from .models import OrderModel, ProductInOrderModel


@api_view(['GET'])
def orders_view(request):
    orders = OrderModel.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def order_in_product_view(request):
    product_in_order = ProductInOrderModel.objects.all()
    serializer = ProductInOrderSerializer(product_in_order, many=True)
    return Response(data=serializer.data)


# Create your views here.
