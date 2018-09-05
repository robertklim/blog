from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ArticleCreateForm
from .models import Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleCreateForm
    template_name = 'articles/article_create_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Now I can customize form
        instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:article-list')

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

class ArticleDetailView(DetailView):
    def get_queryset(self):
        return Article.objects.all()

class ArticleListView(ListView):
    def get_queryset(self):
        return Article.objects.all()

class ArticleUpdateView(UpdateView):
    form_class = ArticleCreateForm
    template_name = 'articles/article_update_form.html'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
