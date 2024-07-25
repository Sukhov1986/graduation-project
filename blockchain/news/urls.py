from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:news_id>', views.article, name='article'),
    path('add-article/', views.add_article, name='add_article'),
]
