from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, verbose_name='пользователь')
    name = models.CharField(max_length=200, blank=True, verbose_name='имя')
    email = models.EmailField(max_length=500, blank=True)
    username = models.CharField(max_length=200, blank=True, verbose_name='имя пользователя')
    info = models.TextField(blank=True, verbose_name='информация')
    image = models.ImageField(upload_to='profiles/', default='profiles/8380015.jpg', verbose_name='изображение')
    social_vk = models.CharField(max_length=200, blank=True, verbose_name='социальная сеть vk')
    social_facebook = models.CharField(max_length=200, blank=True, verbose_name='социальная сеть facebook')
    social_twitter = models.CharField(max_length=200, blank=True, verbose_name='социальная сеть twitter')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'Профили'



class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='отправитель')
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='messages', verbose_name='получатель')
    content = models.TextField( verbose_name='сообщение')
    is_read = models.BooleanField(default=False, verbose_name='прочитано')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}'

    class Meta:
        ordering = ['is_read', '-created']
        verbose_name = 'сообщение'
        verbose_name_plural = 'Сообщения'




