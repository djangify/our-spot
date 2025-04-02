from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),
    path('search/', views.search, name='search'),
]