from django.db import models

# Create your models here.
class Fish(models.Model):
    species_name = models.TextField(null=True)
    scientific_name = models.TextField(null=True)
    rarity = models.PositiveSmallIntegerField(null=True)
    location = models.TextField(null=True)
    noaa_fisheries_region = models.TextField(null=True)
    population = models.TextField(null=True)
    physical_description = models.TextField(null=True)
    biology = models.TextField(null=True)
    taste = models.TextField(null=True)
    texture = models.TextField(null=True)
    species_illustration_photo = models.JSONField(null = True)
    image_gallery = models.JSONField(null = True)

    def __str__(self):
        return self.species_name

# class Species_illustration_photo:
#     fish = models.ForeignKey(Fish, on_delete=models.CASCADE, related_name="species_illustration_photo")
#     src = models.TextField()
#     alt = models.TextField()
#     title = models.TextField()


# class Image_gallery:
#     fish = models.ForeignKey(Fish, on_delete=models.CASCADE, related_name="image_gallery")
#     src = models.TextField()
#     alt = models.TextField()
#     title = models.TextField()

    
    



