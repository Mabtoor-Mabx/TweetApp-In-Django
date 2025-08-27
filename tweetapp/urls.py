# Urls For Pages in Website
from django.urls import path
from . import views

urlpatterns = [
    # Home / Feed
    path('', views.index, name='index'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Tweets
    path('tweet/new/', views.create_tweet, name='create_tweet'),
    path('tweet/<int:pk>/', views.tweet_detail, name='tweet_detail'),
    path('tweet/<int:pk>/edit/', views.tweet_edit, name='edit_tweet'),
    path('tweet/<int:pk>/delete/', views.tweet_delete, name='delete_tweet'),

    # Profile
    path('profile/', views.profile, name='profile'),
]
