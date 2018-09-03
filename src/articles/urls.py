from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDetailView, 
    ArticleListView,
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='article-detail'),
]
