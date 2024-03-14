from django import views
from django.urls import path
from .views import TravelListView, TravelDetailView
from django.conf import settings
from django.conf.urls import static
from . import views

urlpatterns = [
    path('detail/<int:pk>/',TravelDetailView.as_view(),name='detail'),
    path('list/',TravelListView.as_view(), name="list"),
    path( ' ', views.home, name='home'),
    path('travels/', views.travels_list, name='travels_list'),
    path('travels/create/', views.travel_create, name='travel_create'),
    
]  
    