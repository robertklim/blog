from django.urls import path

from .views import (
    ArticleListAPIView,
    ArticleRudAPIView,
)

app_name = 'api-articles'

urlpatterns = [
    path('id/<int:pk>/', ArticleRudAPIView.as_view(), name='article-id-rud'),
    path('slug/<slug:slug>/', ArticleRudAPIView.as_view(), name='article-slug-rud'),
    path('list/', ArticleListAPIView.as_view(), name='article-list'),
]
