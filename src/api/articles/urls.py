from django.urls import path

from .views import (
    ArticleCreateAPIView,
    ArticleGetKeywordsAPIView,
    ArticleListAPIView,
    ArticleRudAPIView,
)

app_name = 'api-articles'

urlpatterns = [
    path('id/<int:pk>/', ArticleRudAPIView.as_view(), name='article-id-rud'),
    path('slug/<slug:slug>/', ArticleRudAPIView.as_view(), name='article-slug-rud'),
    path('add/', ArticleCreateAPIView.as_view(), name='article-create'),
    path('list/', ArticleListAPIView.as_view(), name='article-list'),
    path('keywords/', ArticleGetKeywordsAPIView.as_view(), name='article-keywords'),
]
