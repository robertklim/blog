from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView, 
    ArticleListView,
    ArticleUpdateView,
    UserArticleListView,
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('user/<str:username>/', UserArticleListView.as_view(), name='user-article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<slug:slug>/edit/', ArticleUpdateView.as_view(), name='article-edit'),
    path('<slug:slug>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]
