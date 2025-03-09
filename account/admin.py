from django.contrib import admin
from .models import Profile


# Display profile elements in admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "photo"]
    raw_id_fields = ["user"]

    
