from django.db import models
from decimal import Decimal


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'категория'


class Crypto(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    short_name = models.CharField(max_length=50, verbose_name='тикер')
    image = models.ImageField(upload_to='crypto/images/', verbose_name='изображение')
    last_updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='cryptos', blank=True, verbose_name='категория')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'криптовалюта'
        verbose_name_plural = 'Криптовалюты'
