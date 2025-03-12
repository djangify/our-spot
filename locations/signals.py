from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Location
from PIL import Image
import os

@receiver(post_save, sender=Location)
def create_thumbnail(sender, instance, created, **kwargs):
    """
    Create thumbnail for location images on save if it doesn't exist
    """
    # Only process if we have an image but no thumbnail
    if instance.image and not instance.thumbnail:
        # Get the image path
        image_path = instance.image.path
        # Open the image
        img = Image.open(image_path)
        # Create a thumbnail version
        img.thumbnail((400, 300), Image.LANCZOS)
        
        # Generate thumbnail path
        thumbnail_dir = os.path.join('media', 'locations', 'thumbnails')
        os.makedirs(thumbnail_dir, exist_ok=True)
        
        # Save with the same filename but in thumbnails directory
        filename = os.path.basename(image_path)
        thumbnail_path = os.path.join(thumbnail_dir, filename)
        
        # Save the thumbnail
        img.save(thumbnail_path, 'WEBP', quality=75)
        
        # Update the model's thumbnail field (without triggering another save)
        Location.objects.filter(pk=instance.pk).update(
            thumbnail=f'locations/thumbnails/{filename}'
        )
        