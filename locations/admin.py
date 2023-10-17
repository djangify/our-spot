from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "image",
    )
    list_filter = ("location_types",)
