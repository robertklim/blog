from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Article

class ArticleDetailView(DetailView):
    def get_queryset(self):
        return Article.objects.all()

class ArticleListView(ListView):
    def get_queryset(self):
        return Article.objects.all()
