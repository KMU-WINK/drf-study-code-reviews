from django.contrib import admin

# Register your models here.
from account.models import AuthUser

admin.site.register(AuthUser)