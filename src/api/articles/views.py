from articles.models import Article
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
)

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


class ArticleRudView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    lookup_fields = ('pk', 'slug')
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Article.objects.all()