from django.urls import path
from . import views

urlpatterns = [
    path('users_view/', views.users_view),

]