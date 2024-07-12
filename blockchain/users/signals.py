from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Profile


def profile_updated(sender, instance, created, **kwargs):
    print('Profile Saved')


def delete_user(sender, instance, **kwargs):
    print("Delete")


post_save.connect(profile_updated, sender=Profile)
post_delete.connect(delete_user, sender=Profile)
