from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Plant
from .permissions import IsAuthorOrReadOnly
from .serializer import PlantSerializer

# Create your views here.

class PlantsList(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer