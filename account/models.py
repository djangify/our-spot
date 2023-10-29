from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField


# Database model for users profile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='followers', blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = ResizedImageField(
        size=[300, 300],
        quality=75,
        upload_to="account/",
        force_format="WEBP",
        blank=False,
    )

    def __str__(self):
        return f'Profile of {self.user.username}'

    def follow(self, user_to_follow):
            if user_to_follow != self.user:
                self.following.add(user_to_follow)

    def unfollow(self, user_to_unfollow):
        self.following.remove(user_to_unfollow)

    def is_following(self, user):
        return self.following.filter(id=user.id).exists()

