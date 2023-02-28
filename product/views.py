from rest_framework.decorators import api_view
from rest_framework.response import Response




@api_view(['GET'])
def test(request):
    data = {
        'text': 'Hello World!'
    }
    return Response(data=data)
