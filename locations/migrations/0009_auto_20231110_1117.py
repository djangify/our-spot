# Generated by Django 3.2.22 on 2023-11-10 11:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0008_alter_location_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='location_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
