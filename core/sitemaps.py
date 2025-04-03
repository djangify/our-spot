# core/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from locations.models import Location
from django.contrib.auth.models import User
from core.models import Page
from blog.models import Post

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    
    def items(self):
        return ['core:home', 'account:login', 'account:register', 'account:user_list', 
                'locations:locations']
    
    def location(self, item):
        return reverse(item)

class LocationSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7
    
    def items(self):
        return Location.objects.all()
    
    def lastmod(self, obj):
        return obj.posted_date

class UserSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.3
    
    def items(self):
        # Add ordering to eliminate the warning
        return User.objects.filter(is_active=True).order_by('id')
    
    def location(self, obj):
        return reverse('account:user_detail', args=[obj.username])
    

class PageSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6
    
    def items(self):
        return Page.objects.filter(is_active=True)
    
    def lastmod(self, obj):
        return obj.publish_date

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7
    
    def items(self):
        return Post.objects.filter(status='published')
    
    def lastmod(self, obj):
        return obj.publish_date
    