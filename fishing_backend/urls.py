from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

urlpatterns = [
    path('fish/', views.FishList.as_view(), name='fish_list'),
    path('fish/<int:pk>/', views.FishDetail.as_view(), name="fish_detail")

]