from django.urls import path
from . import views

urlpatterns = [
    path('orders_view/', views.orders_view),
    path('order_in_product/', views.order_in_product_view),

]