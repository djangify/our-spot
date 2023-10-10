from django.contrib import admin
from .models import Locations


@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = (
        
        "title",
        "description",
        "image",
    )
    list_filter = ("location_type",)
