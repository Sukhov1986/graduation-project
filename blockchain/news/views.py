from django.shortcuts import render
from .models import News


def news(request):
    articles = News.objects.all().order_by('-published_date')
    return render(request, 'news/news.html', {'articles': articles})
