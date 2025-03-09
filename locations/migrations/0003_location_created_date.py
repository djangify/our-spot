# Generated by Django 5.1 on 2025-03-09 14:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_alter_location_posted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
