from rest_framework import serializers

from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

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
        ]
        read_only_fields = ['author']

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)
