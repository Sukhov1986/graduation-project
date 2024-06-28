from django.shortcuts import render, get_object_or_404
from .models import News


def news(request):
    articles = News.objects.all().order_by('-published_date')
    return render(request, 'news/news.html', {'articles': articles})


def article(request, news_id):
    st = get_object_or_404(News, pk=news_id)
    return render(request, 'news/article.html', {'st': st})
