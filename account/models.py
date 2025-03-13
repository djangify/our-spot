from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField


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
    