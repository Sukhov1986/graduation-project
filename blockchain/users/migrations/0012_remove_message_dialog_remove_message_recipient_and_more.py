# Generated by Django 5.0.7 on 2024-08-15 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_message_dialog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='dialog',
        ),
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Dialog',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]