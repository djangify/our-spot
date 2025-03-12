from django.core.management.base import BaseCommand
from locations.models import Location
from PIL import Image
import os

class Command(BaseCommand):
    help = 'Optimize existing images and create thumbnails'

    def handle(self, *args, **options):
        locations = Location.objects.all()
        self.stdout.write(f"Processing {locations.count()} locations...")
        
        for location in locations:
            # Process each image
            if location.image and not location.thumbnail:
                self.stdout.write(f"Processing: {location.title}")
                try:
                    # Get the image path
                    image_path = location.image.path
                    
                    # Create thumbnail directory if it doesn't exist
                    thumbnail_dir = os.path.join('media', 'locations', 'thumbnails')
                    os.makedirs(thumbnail_dir, exist_ok=True)
                    
                    # Generate thumbnail filename
                    filename = os.path.basename(image_path)
                    thumbnail_path = os.path.join(thumbnail_dir, filename)
                    
                    # Open the image and create thumbnail
                    img = Image.open(image_path)
                    img.thumbnail((400, 300), Image.LANCZOS)
                    
                    # Save the thumbnail
                    img.save(thumbnail_path, 'WEBP', quality=75)
                    
                    # Update the model (without triggering signals)
                    Location.objects.filter(pk=location.pk).update(
                        thumbnail=f'locations/thumbnails/{filename}'
                    )
                    
                    self.stdout.write(self.style.SUCCESS(f"✓ Created thumbnail for {location.title}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"✗ Error processing {location.title}: {str(e)}"))
        
        self.stdout.write(self.style.SUCCESS("Image optimization complete!"))