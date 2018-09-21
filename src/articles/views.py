from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from functools import reduce

from .forms import ArticleCreateForm
from .models import Article

import operator

class ArticleCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = ArticleCreateForm
    template_name = 'articles/article_create_form.html'
    success_message = 'New article created!'

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Now I can customize form
        instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles:article-list')

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

    # def get_queryset(self):
    #     return Article.objects.filter(author=self.request.user)

class ArticleDetailView(DetailView):
    def get_queryset(self):
        return Article.objects.all()

class ArticleListView(ListView):
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.all()

class ArticleSearchListView(ArticleListView):
    def get_queryset(self):
        result = super(ArticleSearchListView, self).get_queryset()
        
        query = self.request.GET.get('q')
        if not query:
            query = self.kwargs.get('q')
        
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(body__icontains=q) for q in query_list))
            )
        
        return result

class UserArticleListView(ListView):
    template_name = 'articles/user_article_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(author=user)

class ArticleUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articles/article_update_form.html'
    success_message = '%(title)s article updated!'

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

    # def get_queryset(self):
    #     return Article.objects.filter(author=self.request.user)
