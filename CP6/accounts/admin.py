from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.
CustomUser = get_user_model()
class CustomUserAdmin(UserAdmin):
    
    add_forms = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','first_name','last_name','age','is_staff','is_superuser']


admin.site.register(CustomUser,CustomUserAdmin)