from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("", include("core.urls", namespace="core")),
    path("locations/", include("locations.urls")),
    path("blog/", include("blog.urls", namespace="blog")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)