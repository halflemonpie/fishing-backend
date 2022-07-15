from django.shortcuts import render
from django.http import JsonResponse

from fishing_backend.serializers import FishSerializer
from .models import Fish
from rest_framework import generics

# Create your views here.
class FishList(generics.ListCreateAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

class FishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

