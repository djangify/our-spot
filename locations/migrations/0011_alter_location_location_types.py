# Generated by Django 5.1 on 2025-04-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0010_alter_location_location_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_types',
            field=models.CharField(choices=[('africa', 'Africa'), ('america', 'America'), ('asia', 'Asia'), ('caribbean', 'Caribbean'), ('central_america', 'Central America'), ('england', 'England'), ('europe', 'Europe'), ('middle_east', 'Middle East'), ('wales', 'Wales'), ('oceanic', 'Oceanic'), ('scotland', 'Scotland')], default='Africa', max_length=50),
        ),
    ]
