from django.contrib import admin
from .models import OrderModel, ProductInOrderModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'id_user', 'sum_order',)
    search_fields = ('id_user',)
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'


@admin.register(ProductInOrderModel)
class ProductInOrderAdmin(admin.ModelAdmin):

    list_display = ('id_order', 'id_product', 'quantity',)
    empty_value_display = '-пусто-'