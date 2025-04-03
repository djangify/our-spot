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
    path('policy/moderation', views.moderation_policy, name='moderation_policy'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views'),
    path('policy/advertising', views.advertising_policy, name='advertising_policy'),
    path('policy/cookies', views.cookies_policy, name='cookies_policy'),
    path('policy/privacy', views.privacy_policy, name='privacy_policy'),
    path('policy/terms', views.terms_policy, name='terms_policy'),
    path('policy/', views.policies_index, name='policies_index'),
    path('report/', views.report_content, name='report_content'),
]
