from accounts.Api.serializers import AccountSerializer
from rest_framework.viewsets import ModelViewSet
from accounts.models import account
from accounts.api.views import AccountListCreateView

class AccountListCreateView(ModelViewSet):
    queryset = account.objects.all()
    serializer_class = AccountSerializer