from django.db import models

class Accounts(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.login
