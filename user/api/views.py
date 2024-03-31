from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from user.models import CustomUser
from .serializers import CustomUserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('token')  # Obter o token do response data
        if token:
            return Response({'token': token})
        else:
            user = request.user  # Obter o usuário autenticado
            token, created = Token.objects.get_or_create(user=user)  # Criar ou obter o token
            return Response({'token': token.key})
