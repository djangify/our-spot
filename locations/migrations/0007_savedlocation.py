# Generated by Django 5.1 on 2025-04-02 12:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_location_thumbnail_alter_location_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_date', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_by', to='locations.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_locations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-saved_date'],
                'unique_together': {('user', 'location')},
            },
        ),
    ]
