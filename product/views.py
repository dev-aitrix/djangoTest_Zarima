from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import ProductModel


@api_view(['GET'])
def products_view(request):
    products = ProductModel.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)


