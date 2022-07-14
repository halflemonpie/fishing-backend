from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class Fish(models.Model):
    species_name = models.TextField()
    scientific_name = models.TextField()
    rarity = models.PositiveSmallIntegerField()
    location = models.TextField()
    noaa_fisheries_region = models.TextField()
    population = models.TextField()
    physical_description = models.TextField()
    biology = models.TextField()
    taste = models.TextField()
    texture = models.TextField()
    

    def __str__(self):
        return self.species_name

class Species_illustration_photo:
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE, related_name="species_illustration_photo")
    src = models.TextField()
    alt = models.TextField()
    title = models.TextField()


class Image_gallery:
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE, related_name="image_gallery")
    src = models.TextField()
    alt = models.TextField()
    title = models.TextField()

    
    



