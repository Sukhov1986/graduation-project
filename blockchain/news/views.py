from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import News
from .forms import NewsForm
from django.contrib import messages
from django.shortcuts import render, redirect


def news(request):
    articles = News.objects.all().order_by('-published_date')
    return render(request, 'news/news.html', {'articles': articles})


def article(request, news_id):
    st = get_object_or_404(News, pk=news_id)
    return render(request, 'news/article.html', {'st': st})


@login_required(login_url='login')
def add_article(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья добавлена  успешно')
            return redirect('news')
        else:
            messages.error(request, 'В процессе добавления  произошла ошибка')
            form = NewsForm()

    context = {'form': form}
    return render(request, 'news/add_article.html', context)
