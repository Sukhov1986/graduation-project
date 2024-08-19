from django.db import models
from decimal import Decimal


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'категория'


class Crypto(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='crypto/images/')
    last_updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='cryptos', blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'криптовалюта'
        verbose_name_plural = 'Криптовалюты'
