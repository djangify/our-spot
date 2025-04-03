from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, LocationSitemap, UserSitemap, PageSitemap, BlogSitemap

app_name = 'core'


sitemaps = {
    'static': StaticViewSitemap,
    'locations': LocationSitemap,
    'users': UserSitemap,
    'pages': PageSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),
    path('search/', views.search, name='search'),
    path('report/', views.report_content, name='report_content'),
    path('dashboard/', views.moderation_dashboard, name='dashboard'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
    path('policy/moderation', views.moderation_policy, name='moderation_policy'),
    path('report/', views.report_content, name='report_content'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views'),
]