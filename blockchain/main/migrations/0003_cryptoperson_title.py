# Generated by Django 5.0.7 on 2024-08-22 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_cryptoperson_options_remove_cryptoperson_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptoperson',
            name='title',
            field=models.CharField(default='Не указано', max_length=200, verbose_name='заголовок'),
        ),
    ]
