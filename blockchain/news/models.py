from django.db import models

from users.models import Profile


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    content = models.TextField( verbose_name='контент')
    image = models.ImageField(upload_to='news/images/', default='news/images//1659682472110977919.jpg', verbose_name='изображение')
    likes = models.ManyToManyField(Profile, related_name='liked_articles', blank=True, verbose_name='лайк')
    published_date = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='комментатор')
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='новость')
    comment = models.TextField(blank=True, verbose_name='комментарий')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.owner} on {self.news}'

    class Meta:
        unique_together = [['owner', 'news']]
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
