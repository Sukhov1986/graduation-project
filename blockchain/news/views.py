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
    user_has_commented = False

    if request.user.is_authenticated:
        user_has_commented = Comments.objects.filter(owner=request.user.profile, news=st).exists()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comm = form.save(commit=False)
                comm.owner = request.user.profile
                comm.news = st
                comm.save()
                messages.success(request, 'Ваш отзыв оставлен успешно')
                return redirect(request.path_info)
        else:
            return redirect('login')

    context = {
        'st': st,
        'comments': comments,
        'form': form,
        'user_has_commented': user_has_commented
    }
    return render(request, 'news/article.html', context)

@login_required(login_url='login')
def like_news(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    if request.user.is_authenticated:
        profile = request.user.profile
        if news_item.likes.filter(id=profile.id).exists():
            news_item.likes.remove(profile)
        else:
            news_item.likes.add(profile)

    return redirect('article', news_id=pk)
