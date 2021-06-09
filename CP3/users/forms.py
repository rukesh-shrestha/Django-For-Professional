from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields= UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=get_user_model()
        fields= UserChangeForm.Meta.fields