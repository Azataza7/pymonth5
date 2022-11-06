from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserLoginSerializer, UserRegisterSerializer


@api_view(['POST'])
def register_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_view(request):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if not user:
        return Response(status=status.HTTP_403_FORBIDDEN,
                        data={'message': 'User data are wrong'})
    try:
        token = Token.objects.get(user=user)
    except:
        token = Token.objects.create(user=user)
    return Response(data={'key': token.key})
