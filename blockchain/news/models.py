from django.db import models

from users.models import Profile


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/images/', default='news/images//1659682472110977919.jpg')
    likes = models.ManyToManyField(Profile, related_name='liked_articles', blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title


class Comments(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.owner} on {self.news}'

    class Meta:
        unique_together = [['owner', 'news']]
