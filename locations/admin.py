from django.contrib import admin
from .models import Location, LikeLocation


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "image",
    )
    list_filter = ("location_types",)


admin.site.register(LikeLocation)
