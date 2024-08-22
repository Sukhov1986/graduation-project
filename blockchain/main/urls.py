from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('person/<int:person_id>/', views.person_detail, name='person_detail'),
]
