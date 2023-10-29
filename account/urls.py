from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('', include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("edit/", views.edit, name="edit"),
    path('users/', views.user_list, name='user_list'),
    path('followers_count', views.followers_count, name='followers_count'),
    path('users/<username>/', views.user_detail, name='user_detail'),
]
