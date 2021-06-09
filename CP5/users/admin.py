from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

CustomModel = get_user_model()
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomModel
    list_display=['username','email','first_name','last_name','age','is_staff']

admin.site.register(CustomModel,CustomUserAdmin)
