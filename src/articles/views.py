from django.shortcuts import render
from django.views.generic import ListView

class ArticleListView(ListView):
    def get(self, request):
        return render(request, 'articles/article_list.html')