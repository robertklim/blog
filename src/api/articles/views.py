from articles.models import Article
from collections import Counter
from django.shortcuts import get_object_or_404
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly
from .serializers import ArticleSerializer

class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if field in self.kwargs:
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class ArticleCreateAPIView(CreateAPIView):
    lookup_field = 'pk'
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleGetKeywordsAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        articles = Article.objects.all()
        text, text_cleared = '', ''

        for article in articles:
            text += article.body + ' '

        text = text.lower()
        
        tokenizer = RegexpTokenizer(r'\w+')
        word_tokens = tokenizer.tokenize(text)
        stop_words = set(stopwords.words('english'))
        
        filtered_text = [w for w in word_tokens if not w in stop_words]

        res = Counter(filtered_text).most_common(10)
        
        return Response(res)

class ArticleListAPIView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()

class ArticleRudAPIView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    lookup_fields = ('pk', 'slug')
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Article.objects.all()
