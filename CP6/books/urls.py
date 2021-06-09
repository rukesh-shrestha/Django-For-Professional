from django.contrib import admin
from django.urls import path,include
from .views import BookPageView,BookDetailView,SearchList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<uuid:pk>',BookDetailView.as_view(),name='book_detial'),
    path('',BookPageView.as_view(),name='book_list'),
    path('search/',SearchList.as_view(),name = 'search'),
]
