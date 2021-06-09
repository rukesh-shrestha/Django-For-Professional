from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'