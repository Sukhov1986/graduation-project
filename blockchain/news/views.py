from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import News, Comments
from django.shortcuts import render, redirect
from .utils import search_content, paginate
from .forms import CommentForm
from django.contrib import messages


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
    comments = Comments.objects.filter(news=st).order_by('-created')
    form = CommentForm()

    user_has_commented = Comments.objects.filter(owner=request.user.profile, news=st).exists()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.owner = request.user.profile
            comm.news = st
            if not user_has_commented:
                comm.save()
                messages.success(request, 'Комментарий оставлен успешно')
                return redirect('article', news_id=news_id)
            else:
                messages.error(request, 'Вы уже оставляли комментарий к этой новости')
                return redirect('article', news_id=news_id)
    context = {
        'st': st,
        'comments': comments,
        'form': form
    }
    return render(request, 'news/article.html', context)
