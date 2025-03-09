# Generated by Django 5.1 on 2025-03-09 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('content', models.TextField(verbose_name='Blog Content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/images/')),
                ('external_image_url', models.URLField(blank=True, help_text='External URL for product image (jpg/png only)', max_length=500, null=True)),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='blog/thumbnails/')),
                ('ad_type', models.CharField(choices=[('none', 'No Advertisement'), ('adsense', 'Google AdSense'), ('banner', 'Banner Image')], default='none', max_length=10)),
                ('ad_code', models.TextField(blank=True)),
                ('ad_image', models.ImageField(blank=True, null=True, upload_to='blog/ads/')),
                ('ad_url', models.URLField(blank=True)),
                ('meta_title', models.CharField(blank=True, help_text='SEO Title (60 characters max)', max_length=60)),
                ('meta_description', models.CharField(blank=True, help_text='SEO Description (160 characters max)', max_length=160)),
                ('meta_keywords', models.CharField(blank=True, help_text='Comma-separated keywords', max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
            options={
                'ordering': ['-publish_date', '-created'],
            },
        ),
    ]
