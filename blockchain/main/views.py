from django.conf import settings
import requests
from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')

