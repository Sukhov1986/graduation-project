from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django import forms
from .models import Profile
from django.forms import ModelForm


class ProfileModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'info', 'image', 'social_vk', 'social_facebook', 'social_twitter']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            field.widget.attrs.update({'placeholder': field.label})
