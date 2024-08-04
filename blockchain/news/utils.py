from django.db.models import Q

from .models import News

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate(request, articles, result):
    page = request.GET.get('page', 1)
    paginator = Paginator(articles, result)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    current_page = int(page)
    left_index = max(current_page - 3, 1)
    right_index = min(current_page + 4,
                      paginator.num_pages + 1)
    custom_range = range(left_index, right_index)
    return custom_range, articles


def search_content(request):
    search_news = ''
    if request.GET.get('search_news'):
        search_news = request.GET.get('search_news')
    articles = News.objects.filter(Q(title__icontains=search_news) | Q(content__icontains=search_news)).order_by(
        '-published_date')
    return articles, search_news
