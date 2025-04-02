from django.contrib import admin

from core.views import send_moderation_action_notification
from .models import HomePage, HeroBanner, Page
from .models import Report

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
    

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_content_type', 'report_type', 'reporter', 'status', 'created_at')
    list_filter = ('report_content_type', 'report_type', 'status', 'created_at')
    search_fields = ('reporter__username', 'details', 'reason')
    readonly_fields = ('reporter', 'content_type', 'object_id', 'report_type', 'reason', 'details', 'created_at')
    
    fieldsets = (
        ('Report Information', {
            'fields': ('reporter', 'report_content_type', 'report_type', 'reason', 'details', 'created_at')
        }),
        ('Content', {
            'fields': ('content_type', 'object_id')
        }),
        ('Review', {
            'fields': ('status', 'reviewed_by', 'review_notes', 'updated_at')
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields
        return ()
        
    def save_model(self, request, obj, form, change):
        if change and 'status' in form.changed_data:
            # Set the reviewer to the current admin user when status changes
            obj.reviewed_by = request.user
            
            # If status changed to "actioned" or "dismissed", send notification email
            if obj.status in ['actioned', 'dismissed']:
                send_moderation_action_notification(obj)
        
        super().save_model(request, obj, form, change)