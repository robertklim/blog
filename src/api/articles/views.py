from articles.models import Article

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
)

from .serializers import ArticleSerializer

class ArticleRudView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()
