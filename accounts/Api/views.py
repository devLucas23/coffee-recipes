from rest_framework.viewsets import ModelViewSet
from accounts.Api.serializers import AccountSerializer
from accounts.models import Accounts

class AccountListCreateView(ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer

    