# Generated by Django 4.0.6 on 2022-07-14 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishing_backend', '0006_fish_image_gallery_fish_species_illustration_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='biology',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='noaa_fisheries_region',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='physical_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='population',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='rarity',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='scientific_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='species_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='taste',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='texture',
            field=models.TextField(null=True),
        ),
    ]
