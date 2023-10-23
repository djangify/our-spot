from django.contrib import admin
from .models import Location, Comment, Tag

# Displays elements in admin to add location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "description",
        "image",
    )
    list_filter = ("location_types",)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comment)
admin.site.register(Tag)
