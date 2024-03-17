from rest_framework.viewsets import ModelViewSet
from recipes.models import Recipes
from recipes.Api.serializers import RecipeSerializer

class RecipeListCreateView(ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer