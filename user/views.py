from django.contrib.auth import authenticate

from rest_framework import status,permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenBlacklistView

from user.api.serializers import (
    CustomTokenObtainPairSerializer, CustomUserSerializer,RefreshTokenSerializer)
from user.models import User

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        # rol = request.data.get('rol', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            # rol=rol,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': 'Bearer '+login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesión Existoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
class LogoutView(TokenBlacklistView):
    serializer_class = RefreshTokenSerializer
    # permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)