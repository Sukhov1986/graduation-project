from django.urls import path
from . import views

urlpatterns = [
    # path('', views.profiles, name='profiles'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('account/', views.user_account, name='account'),
    path('edit-account/', views.edit_account, name='edit-account'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<int:pk>/', views.view_message, name='message'),
    path('create-message/<int:pk>/', views.create_message, name='create_message'),
]
