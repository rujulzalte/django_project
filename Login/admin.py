from django.contrib import admin
from .models import UserLogin
# Register your models here.


# admin.site.register(UserLogin)

@admin.register(UserLogin)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'password', 'Phone_no', 'state']
