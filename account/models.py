from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField

"""
Database model for users profile
"""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15, default="Usef")
    last_name = models.CharField(max_length=15, default="Usefsson")
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(
        max_length=150, default="Currently no bio", blank=True)
    photo = CloudinaryField('image', default='placeholder')
    country = CountryField(
        max_length=30, blank_label="(Where's your SPOT?)", blank=True
    )

    def __str__(self):
        return f'Profile of {self.user} | {self.first_name} {self.last_name}'
