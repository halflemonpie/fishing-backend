# Generated by Django 4.0.6 on 2022-07-14 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishing_backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='image_gallery',
        ),
        migrations.RemoveField(
            model_name='fish',
            name='species_illustration_photo',
        ),
    ]
