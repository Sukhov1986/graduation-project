from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ProfileModelForm, MassageForm
from django.contrib.auth.decorators import login_required


def register_user(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Учетная запись создана успешно')
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'В процессе регистрации произошла ошибка')
            # print(form.errors)

    context = {'form': form, 'title': "Регистрация"}
    return render(request, 'users/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Такого пользователя не существует")
            return render(request, 'users/login.html')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Не корректные данные для входа')
    context = {'title': "Авторизация"}
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'Вы вышли из профиля')
    return redirect('login')





def profile(request, pk):
    pr = get_object_or_404(Profile, pk=pk)
    return render(request, 'users/profile.html', {'profile': pr})


@login_required(login_url='login')
def user_account(request):
    prof = request.user.profile
    context = {
        'profile': prof,
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    prof = request.user.profile
    form = ProfileModelForm(instance=prof)
    if request.method == 'POST':
        form = ProfileModelForm(request.POST, request.FILES, instance=prof)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def delete_profile(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.success(request, "Профиль успешно удален.")
        return redirect('home')
    return render(request, 'users/delete_profile.html', {'user': user})


@login_required(login_url='login')
def inbox(request):
    pr = request.user.profile
    message_request = pr.messages.all()
    count_message = message_request.filter(is_read=False).count()
    context = {
        'count_message': count_message,
        'message_request': message_request,
    }
    return render(request, 'users/inbox.html', context)


def view_message(request, pk):
    pr = request.user.profile
    message = pr.messages.get(id=pk)
    if message.is_read is False:
        message.is_read = True
        message.save()
    context = {
        'message': message
    }
    return render(request, 'users/message.html', context)


@login_required(login_url='login')
def create_message(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MassageForm
    context = {
        'recipient': recipient,
        'form': form
    }
    return render(request, 'users/message_form.html', context)

