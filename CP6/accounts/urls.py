from django.contrib import admin
from django.urls import path
from .views import SignupPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',SignupPageView.as_view(),name='signup')
]
