from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify

class Article(models.Model):
    title       = models.CharField(max_length=128)
    slug        = models.SlugField(null=True, unique=True, blank=True)
    body        = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    thumbnail   = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('articles:article-list')
