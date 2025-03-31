from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.contrib.auth.models import User


class Profile(models.Model):
    """Database model for users profile"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    about_me = models.TextField(
        blank=True, 
        null=True, 
        max_length=300,
        help_text="Write a brief introduction",
    )
    photo = ResizedImageField(
        size=[300, 300],
        quality=75,
        upload_to="account/",
        force_format="WEBP",
        blank=False,
    )

    def __str__(self):
        return self.user.username

import uuid
from django.utils import timezone
from datetime import timedelta

class EmailVerificationToken(models.Model):
    """Model for email verification tokens"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    reminder_sent = models.BooleanField(default=False)
    reminder_sent_at = models.DateTimeField(null=True, blank=True)
    
    def is_valid(self):
        # Token expires after 24 hours
        return self.created_at >= timezone.now() - timedelta(hours=24)
    
    def __str__(self):
        return f"Verification for {self.user.username}"


class UserFollow(models.Model):
    """Model to track user follow relationships"""
    user = models.ForeignKey(
        User, 
        related_name='following_set',
        on_delete=models.CASCADE
    )
    followed_user = models.ForeignKey(
        User,
        related_name='followers_set',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'followed_user')
        ordering = ['-created_at']
        verbose_name = 'User Follow'
        verbose_name_plural = 'User Follows'
    
    def __str__(self):
        return f"{self.user.username} follows {self.followed_user.username}"

# Add these methods to extend the User model functionality
def add_to_class(cls, name, value):
    """Add a method to an existing class."""
    if not hasattr(cls, name):
        setattr(cls, name, value)

# Method to follow a user
def follow(self, user):
    """Follow a user"""
    if self != user:  # Can't follow yourself
        return UserFollow.objects.get_or_create(user=self, followed_user=user)
    return None, False

# Method to unfollow a user
def unfollow(self, user):
    """Unfollow a user"""
    UserFollow.objects.filter(user=self, followed_user=user).delete()

# Method to check if user is following another user
def is_following(self, user):
    """Check if user is following another user"""
    return self.following_set.filter(followed_user=user).exists()

# Method to get all users followed by this user
def get_following(self):
    """Get all users followed by this user"""
    return User.objects.filter(followers_set__user=self)

# Method to get all followers of this user
def get_followers(self):
    """Get all followers of this user"""
    return User.objects.filter(following_set__followed_user=self)

# Add the methods to the User model
add_to_class(User, 'follow', follow)
add_to_class(User, 'unfollow', unfollow)
add_to_class(User, 'is_following', is_following)
add_to_class(User, 'get_following', get_following)
add_to_class(User, 'get_followers', get_followers)