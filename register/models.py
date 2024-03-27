from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmPassword = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name