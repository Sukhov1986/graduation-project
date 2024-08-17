from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:news_id>', views.article, name='article'),
    path('news/<int:pk>/like/', views.like_news, name='like_news'),

]
