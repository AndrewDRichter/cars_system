from django.urls import path
from .views import CarsListView, NewCarCreateView, CarDetailView


urlpatterns = [
    path("", CarsListView.as_view(), name='cars_list'),
    path("new", NewCarCreateView.as_view(), name='new_car'),
    path("<int:pk>", CarDetailView.as_view(), name='car_detail'),
]
