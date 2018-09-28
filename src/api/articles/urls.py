from django.urls import path

from .views import (
    ArticleRudView,
)

app_name = 'api-articles'

urlpatterns = [
    path('id/<int:pk>/', ArticleRudView.as_view(), name='article-id-rud'),
    path('slug/<slug:slug>/', ArticleRudView.as_view(), name='article-slug-rud'),
]
