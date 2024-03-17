from django.db import models

# Create your models here.
class Recipes(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    preparation = models.CharField(max_length=100)
    intensidade = models.IntegerField()

    def __str__(self):
        return self.title