from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import News, Comments
from django.shortcuts import render, redirect
from .utils import search_content, paginate


def news(request):
    articles, search_news = search_content(request)
    custom_range, articles = paginate(request, articles, 3)

    context = {
        'articles': articles,
        'search_news': search_news,
        'custom_range': custom_range,
    }
    return render(request, 'news/news.html', context)


def article(request, news_id):
    st = get_object_or_404(News, pk=news_id)
    comments = Comments.objects.filter(news=st)
    context = {
        'st': st,
        'comments': comments
    }
    return render(request, 'news/article.html', context)
