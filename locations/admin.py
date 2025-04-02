from django.contrib import admin
from .models import Location, Comment, Tag


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description", "image", "posted_date")
    list_filter = ("location_types", "tags")  
    prepopulated_fields = {"slug": ("title",)}
    fields = (
        "title", "slug", "description", "image", "image_alt", 
        "location_types", "posted_date", "user", "likes", "tags"
    )
    filter_horizontal = ("tags",)  


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "location",
        "text",
        "created_at",
        "updated_at",
    )
    list_filter = ("user", "location", "created_at")
    fields = ("user", "location", "text", "created_at", "updated_at")
    readonly_fields = ()  
    
    # Allow changing dates in the admin panel
    def get_readonly_fields(self, request, obj=None):
        # If the user is a superuser, they can edit all fields
        if request.user.is_superuser:
            return []
        # Otherwise, make dates read-only for regular admins
        return ["created_at", "updated_at"]