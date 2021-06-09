from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SignUpPage

urlpatterns = [
    path('signup/',SignUpPage.as_view(),name='signup'),
]
