from django.urls import path
from .views import cars_view, new_car_view


urlpatterns = [
    path("", cars_view, name='cars_list'),
    path("new", new_car_view, name='new_car'),
]
