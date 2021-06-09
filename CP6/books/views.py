from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView,DetailView
from .models import Book
from django.db.models import Q

# Create your views here.
class BookPageView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Book
    template_name = 'book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchList(ListView):
    model = Book
    template_name = 'search.html'
    # queryset = Book.objects.filter(title__icontains='API')

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains =query)
        )