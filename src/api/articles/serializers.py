from rest_framework import serializers

from articles.models import Article

from taggit_serializer.serializers import (
    TagListSerializerField,
    TaggitSerializer,
)

import six

class NewTagListSerializerField(TagListSerializerField):
    def to_internal_value(self, value):
        if isinstance(value, six.string_types):
            value = value.split(',')

        if not isinstance(value, list):
            self.fail('not_a_list', input_type=type(value).__name__)

        for s in value:
            if not isinstance(s, six.string_types):
                self.fail('not_a_str')

            self.child.run_validation(s)
        return value

class ArticleSerializer(TaggitSerializer, serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    tags = NewTagListSerializerField()

    class Meta:
        model = Article
        fields = [
            'url',
            'pk',
            'title',
            'slug',
            'body',
            'timestamp',
            'updated',
            'thumbnail',
            'author',
            'tags',
        ]
        read_only_fields = ['author']

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)
