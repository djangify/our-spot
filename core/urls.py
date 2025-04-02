from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),
    path('search/', views.search, name='search'),
    path('report/', views.report_content, name='report_content'),
    path('dashboard/', views.moderation_dashboard, name='dashboard'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
    path('policy/', views.moderation_policy, name='moderation_policy'),
    path('report/', views.report_content, name='report_content'),
]