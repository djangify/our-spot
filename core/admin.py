from django.contrib import admin
from .models import HomePage, HeroBanner, Page


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
        ('Hero Section', {
            'fields': ('main_image', 'heading', 'subheading', 'text', 
                      'button1_text', 'button1_link', 'button2_text', 'button2_link'),
        }),
        ('Page Content', {
            'fields': ('main_content', 'second_content'),
        }),
        ('Settings', {
            'fields': ('is_active',),
        }),
    )
    
    def has_add_permission(self, request):
        # Check if any HomePage objects exist
        if HomePage.objects.exists():
            return False  # If exists, don't allow adding more
        return True  # Otherwise, allow adding one


@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ('text', 'badge_text', 'action_text', 'is_active')
    list_editable = ('is_active',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'publish_date')
    list_filter = ('is_active', 'publish_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
        ('Page Content', {
            'fields': ('title', 'slug', 'content', 'second_content'),
        }),
        ('Publishing Options', {
            'fields': ('is_active', 'publish_date'),
        }),
    )
    