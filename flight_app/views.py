from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

from flight_app.serializers import RegisterSerializer
from flight_app.serializers import UserSerializer

@api_view(['POST'])
def sign_up(request):
    serializer = RegisterSerializer(data=request.data, many=False)
    if serializer.is_valid(raise_exception=True):
        new_user = serializer.create(serializer.validated_data)
        return Response(data=UserSerializer(instance=new_user, many=False).data)



