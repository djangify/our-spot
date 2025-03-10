from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django_resized import ResizedImageField
from django_prose_editor.fields import ProseEditorField


class SEOFields(models.Model):
    """Abstract model for common SEO fields"""
    meta_title = models.CharField(
        max_length=60, blank=True, help_text="SEO Title (60 characters max)"
    )
    meta_description = models.CharField(
        max_length=160, blank=True, help_text="SEO Description (160 characters max)"
    )
    meta_keywords = models.CharField(
        max_length=255, blank=True, help_text="Comma-separated keywords"
    )

    class Meta:
        abstract = True


class HomePage(SEOFields):
    """Model for the home page content"""
    main_image = ResizedImageField(
        size=[1920, 1080],
        quality=75,
        upload_to="home/",
        force_format="WEBP",
        blank=True,
        null=True,
        help_text="Main hero image (1920x1080 recommended)"
    )
    heading = models.CharField(max_length=100, default="Show Your Spot")
    subheading = models.CharField(max_length=200, default="Every Spot Tells A Story")
    text = models.TextField(
        default="Discover hidden gems and share your favorite places with the world. "
        "Whether it's a tranquil nature retreat, a cozy café, or a breathtaking viewpoint - "
        "every spot tells a story. Share yours today."
    )
    button1_text = models.CharField(max_length=50, default="Register Here")
    button1_link = models.CharField(max_length=200, default="/account/register/")
    button2_text = models.CharField(max_length=50, default="Log-In Here")
    button2_link = models.CharField(max_length=200, default="/account/login/")
    main_content = ProseEditorField(blank=True, null=True)
    second_content = ProseEditorField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"

    def __str__(self):
        return "Home Page Content"


class HeroBanner(models.Model):
    """Model for the hero banner/announcement bar"""
    text = models.CharField(max_length=200, default="Discover Featured Spots")
    badge_text = models.CharField(max_length=50, default="New")
    action_text = models.CharField(max_length=100, default="See what's new")
    action_link = models.CharField(max_length=200, default="/locations/locations/")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Hero Banner"
        verbose_name_plural = "Hero Banners"

    def __str__(self):
        return self.text


class Page(SEOFields):
    """Model for standard pages like About, Privacy Policy, etc."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = ProseEditorField(blank=True, null=True)
    second_content = ProseEditorField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:page_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def is_published(self):
        return self.is_active and self.publish_date <= timezone.now()