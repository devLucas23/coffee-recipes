from django.contrib import admin
from accounts.models import Accounts  # <--- import the model

# Register your models here.

admin.site.register(Accounts)  # <--- register the model
