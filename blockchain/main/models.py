from django.db import models

class CryptoPerson(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    title = models.CharField(max_length=200, blank=True, verbose_name='заголовок')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='main/images/', verbose_name='фото')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'персону'
        verbose_name_plural = 'Персоны'
        ordering = ['-published_date']
# Create your models here.
