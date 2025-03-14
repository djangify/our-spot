from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django_resized import ResizedImageField

# Choice Fields to save locations under
LOCATION_TYPES = (
    ("africa", "Africa"),
    ("america", "America"),
    ("asia", "Asia"),
    ("caribbean", "Caribbean"),
    ("europe", "Europe"),
    ("great_britain", "Great Britain"),
    ("middle_east", "Middle East"),
    ("oceanic", "Oceanic"),
)

class Location(models.Model):
    """Creates and manages shared locations"""

    user = models.ForeignKey(
        User, related_name="location_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    description = models.CharField(max_length=500, null=False, blank=False)

    image = ResizedImageField(
        size=[1200, 900],
        quality=75,
        upload_to='locations/',
        blank=False,
        force_format='WEBP'
    )
    thumbnail = ResizedImageField(
        size=[400, 300],
        quality=75,
        upload_to='locations/thumbnails/',
        blank=True,
        null=True,
        force_format='WEBP'
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    location_types = models.CharField(
        max_length=50, choices=LOCATION_TYPES, default="Africa"
    )
    created_date = models.DateTimeField(auto_now_add=True) 
    posted_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name="location_likes", blank=True)

    class Meta:
        ordering = ["-posted_date"]
    
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("locations:location_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # Generate a slug based on the title
        if not self.slug:
            self.slug = slugify(self.title)

        super(Location, self).save(*args, **kwargs)


class Comment(models.Model):
    """Model for comments section"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.text[:40]}"
        
    def save(self, *args, **kwargs):
        # Only update the updated_at time if not explicitly set
        if not self.id and not self.created_at:
            self.created_at = timezone.now()
        if not self.updated_at or self.updated_at == self.created_at:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)
