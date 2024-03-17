from rest_framework.viewsets import ModelViewSet
from register.Api.serializers import RegisterSerializer
from register.models import Register
# Create your views here.

class RegisterListCreateView(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer