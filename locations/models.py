from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django_resized import ResizedImageField
from tinymce.models import HTMLField

# Choice Fields to save locations under
LOCATION_TYPES = (
    ("africa", "Africa"),
    ("america", "America"),
    ("asia", "Asia"),
    ("caribbean", "Caribbean"),
    ("central_america", "Central America"),
    ("england", "England"),
    ("europe", "Europe"),
    ("middle_east", "Middle East"),
    ("wales", "Wales"),
    ("oceanic", "Oceanic"),
    ("scotland", "Scotland"),
)

class Tag(models.Model):
    """Model for tagging locations"""
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Location(models.Model):
    """Creates and manages shared locations"""

    user = models.ForeignKey(
        User, related_name="location_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    description = HTMLField(null=False, blank=False, verbose_name="Location Description")

    image = ResizedImageField(
        size=[1200, 900],
        quality=75,
        upload_to='locations/',
        blank=True,
        null=True,
        force_format='WEBP'
    )
    external_image_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="External URL for photo (if not uploading directly)"
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
    tags = models.ManyToManyField(Tag, blank=True, related_name="locations")
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
    
    def get_image_url(self):
        """Return the appropriate image URL (uploaded or external)"""
        if self.external_image_url:
            return self.external_image_url
        elif self.image:
            return self.image.url
        return None

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

class SavedLocation(models.Model):
    user = models.ForeignKey(
        User,  # Using User directly since it's already imported in your models.py
        on_delete=models.CASCADE,
        related_name='saved_locations'
    )
    location = models.ForeignKey(
        Location,  # This will refer to your Location model in the same file
        on_delete=models.CASCADE,
        related_name='saved_by'
    )
    saved_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'location')
        ordering = ['-saved_date']
    
    def __str__(self):
        return f"{self.user.username} saved {self.location.title}"
