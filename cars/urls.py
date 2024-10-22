from django.urls import path
from .views import CarsListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView


urlpatterns = [
    path("", CarsListView.as_view(), name='cars_list'),
    path("new", NewCarCreateView.as_view(), name='new_car'),
    path("<int:pk>", CarDetailView.as_view(), name='car_detail'),
    path("<int:pk>/update", CarUpdateView.as_view(), name='car_update'),
    path("<int:pk>/delete", CarDeleteView.as_view(), name='car_delete'),
]
