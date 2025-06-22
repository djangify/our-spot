from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve



urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls", namespace="account")),
    path("", include("core.urls", namespace="core")),
    path("locations/", include("locations.urls", namespace="locations")),
    path("blog/", include("blog.urls", namespace="blog")),
    path('tinymce/', include('tinymce.urls')),
    path('static/<path:path>', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
    path('media/<path:path>', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
