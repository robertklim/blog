import os
from os.path import basename

from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify

from rest_framework.reverse import reverse as api_reverse

User = settings.AUTH_USER_MODEL

class Article(models.Model):
    title       = models.CharField(max_length=128)
    slug        = models.SlugField(null=True, unique=True, blank=True)
    body        = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    thumbnail   = models.ImageField(default='default_thumbnail.jpg', blank=True, upload_to='thumbnail_images')
    author      = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def owner(self):
        return self.author

    def snippet(self):
        return self.body[:300] + '...'

    def save(self, *args, **kwargs):
        old_thumbnail = Article.objects.get(pk=self.pk).thumbnail
        if (basename(old_thumbnail.name) != basename(self.thumbnail.name) and basename(old_thumbnail.name) != Article._meta.get_field('thumbnail').default):
            os.remove(os.path.join(settings.MEDIA_ROOT, old_thumbnail.name))
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('articles:article-detail', kwargs={'slug': self.slug})

    def get_api_url(self, request=None):
        return api_reverse('api-articles:article-id-rud', kwargs={'pk': self.pk}, request=request)

    class Meta:
        ordering = ['-timestamp']
