from django.contrib import admin
from .models import Location, Comment


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description", "image", "posted_date")
    list_filter = ("location_types",)
    prepopulated_fields = {"slug": ("title",)}
    fields = ("title", "slug", "description", "image", "image_alt", "location_types", "posted_date", "user", "likes")


@admin.register(Comment)  # Displays comments in admin area
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "location",
        "text",
        "created_at",
    )
    list_filter = ("user", "location", "created_at")

