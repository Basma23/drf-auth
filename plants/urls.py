from django.urls import path

from .views import PlantsList, PlantDetails

urlpatterns = [
    path('', PlantsList.as_view(), name='plants'), # localhost:8000/api/v1/posts
    path('<int:pk>/', PlantDetails.as_view(), name='plant_details') # localhost:8000/api/v1/posts/1
]