from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, EmailVerificationToken, UserFollow

# Custom filter for verification status
class VerificationStatusFilter(admin.SimpleListFilter):
    title = 'verification status'
    parameter_name = 'verification'
    
    def lookups(self, request, model_admin):
        return (
            ('unverified', 'Unverified'),
            ('pending', 'Pending verification'),
            ('verified', 'Verified'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'unverified':
            return queryset.filter(is_active=False)
        elif self.value() == 'pending':
            # Users with verification tokens
            user_ids = EmailVerificationToken.objects.values_list('user_id', flat=True)
            return queryset.filter(id__in=user_ids)
        elif self.value() == 'verified':
            # Active users without verification tokens
            user_ids = EmailVerificationToken.objects.values_list('user_id', flat=True)
            return queryset.filter(is_active=True).exclude(id__in=user_ids)
        return queryset

@admin.register(EmailVerificationToken)
class EmailVerificationTokenAdmin(admin.ModelAdmin):
    list_display = ["user", "token", "created_at"]
    readonly_fields = ["token", "created_at"]
    search_fields = ['user__username', 'user__email']
    actions = ['verify_users']
    
    def verify_users(self, request, queryset):
        for token in queryset:
            user = token.user
            user.is_active = True
            user.save()
            token.delete()
        self.message_user(request, f"{queryset.count()} user(s) have been verified successfully.")
    verify_users.short_description = "Verify selected users"

# Add profile to user admin
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

# Extend the User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active']
    list_filter = ['is_active', 'is_staff', 'date_joined', VerificationStatusFilter]
    actions = ['manually_verify_users']
    
    def manually_verify_users(self, request, queryset):
        # Activate selected users
        updated = queryset.update(is_active=True)
        
        # Remove any verification tokens for these users
        for user in queryset:
            EmailVerificationToken.objects.filter(user=user).delete()
            
        self.message_user(request, f"{updated} user(s) have been manually verified.")
    manually_verify_users.short_description = "Manually verify selected users"

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "photo"]
    raw_id_fields = ["user"]

@admin.register(UserFollow)
class UserFollowAdmin(admin.ModelAdmin):
    list_display = ['user', 'followed_user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'followed_user__username']
    date_hierarchy = 'created_at'
