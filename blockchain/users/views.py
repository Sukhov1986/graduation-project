from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile


def profiles(request):
    pr = Profile.objects.all()
    context = {'profiles': pr}
    return render(request, 'users/index.html', context)


def profile(request, pk):
    pr = get_object_or_404(Profile, pk=pk)
    return render(request, 'users/profile.html', {'profile': pr})
