# Generated by Django 5.1 on 2025-03-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, help_text='Write a brief introduction', max_length=300, null=True),
        ),
    ]
