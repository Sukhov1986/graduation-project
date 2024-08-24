from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from .models import Profile, Message
from django.forms import ModelForm

class MassageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class ProfileModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'info', 'image', 'social_vk', 'social_facebook', 'social_twitter']
        labels = {
            'name': 'Имя',
            'email': 'Электронная почта',
            'username': 'Имя пользователя',
            'info': 'Информация',
            'image': 'Фото',
            'social_vk': 'Ссылка на VK',
            'social_facebook': 'Ссылка на Facebook',
            'social_twitter': 'Ссылка на Twitter',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField(label=None)
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, CaptchaField):
                continue
            field.widget.attrs.update({'class': 'form-control'})
            field.widget.attrs.update({'placeholder': field.label})

