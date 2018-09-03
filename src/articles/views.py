from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .forms import ArticleCreateForm
from .models import Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleCreateForm
    template_name = 'articles/article_create_form.html'

class ArticleDetailView(DetailView):
    def get_queryset(self):
        return Article.objects.all()

class ArticleListView(ListView):
    def get_queryset(self):
        return Article.objects.all()
