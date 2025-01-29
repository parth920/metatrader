from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(MasterLogin)
class PurchaseModelAdmin(admin.ModelAdmin):
    list_display = ("master_login","master_password",
                    "login", "password", "server",)

@admin.register(Server)
class ServerModeladmin(admin.ModelAdmin):
    list_display=("server_name","server_id")



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'pin')