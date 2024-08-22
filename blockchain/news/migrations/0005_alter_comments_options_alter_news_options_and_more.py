# Generated by Django 5.0.7 on 2024-08-22 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_likes'),
        ('users', '0014_alter_message_options_alter_profile_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(blank=True, verbose_name='комментарий'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news', verbose_name='новость'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='комментатор'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(verbose_name='контент'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='news/images//1659682472110977919.jpg', upload_to='news/images/', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_articles', to='users.profile', verbose_name='лайк'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='заголовок'),
        ),
    ]
