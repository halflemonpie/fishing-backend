from asyncore import read
from rest_framework import serializers
from .models import Fish

class FishSerializer(serializers.HyperlinkedModelSerializer):
    fish_detail = serializers.ModelSerializer.serializer_url_field(
        view_name='fish_detail'
    )
    class Meta:
        model = Fish
        fields = ('species_name', 'fish_detail', 'scientific_name', 'rarity', 'location', 'noaa_fisheries_region', 'population', 'physical_description', 'biology', 'taste', 'texture', 'species_illustration_photo', 'image_gallery')