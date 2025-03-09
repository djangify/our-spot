# Generated by Django 5.1 on 2025-03-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, help_text='Write a brief introduction about yourself (max 50 words)', null=True),
        ),
    ]
