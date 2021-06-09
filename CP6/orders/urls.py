
from django.contrib import admin
from django.urls import path,include
from .views import OrdersPageView,Charge


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',OrdersPageView.as_view(),name='orders'),
    path('charge/',Charge,name='charge'),
   
    
] 
