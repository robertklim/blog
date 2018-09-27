from django.urls import path

from .views import (
    ArticleRudView,
)

app_name = 'api-articles'

urlpatterns = [
    path('<int:pk>/', ArticleRudView.as_view(), name='article-rud'),
]
