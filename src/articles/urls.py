from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView, 
    ArticleListView,
    ArticleSearchListView,
    ArticleTagListView,
    ArticleUpdateView,
    ArticleUserListView,
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('user/<str:username>/', ArticleUserListView.as_view(), name='article-user-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('search/', ArticleSearchListView.as_view(), name='article-search-form'),
    path('search/<str:q>/', ArticleSearchListView.as_view(), name='article-search-url'),
    path('tag/<str:tag>/', ArticleTagListView.as_view(), name='article-tag-list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<slug:slug>/edit/', ArticleUpdateView.as_view(), name='article-edit'),
    path('<slug:slug>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]
