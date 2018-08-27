from django.db import models

class Article(models.Model):
    title       = models.CharField(max_length=128)
    slug        = models.SlugField()
    body        = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
