from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import UserModel


@api_view(['GET'])
def users_view(request):
    users = UserModel.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(data=serializer.data)
from django.shortcuts import render

# Create your views here.
