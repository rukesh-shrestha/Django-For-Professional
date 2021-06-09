from django import forms
from accounts.models import CustomUser
from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
CustomUser = get_user_model()
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','first_name','last_name','age','is_staff']

admin.site.register(CustomUser,CustomUserAdmin)