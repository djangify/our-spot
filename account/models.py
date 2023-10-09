from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


"""
Database model for users profile
"""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f'Profile of {self.user}'
