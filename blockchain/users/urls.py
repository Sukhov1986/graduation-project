from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<int:pk>/', views.profile, name='profile'),
]
