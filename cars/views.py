from django.shortcuts import render
from .models import Car, Brand
from .forms import CarForm

def cars_view(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    if request.method == 'GET':
        search = request.GET.get("search", None)
        brand = request.GET.get("brand_select", None)
        print(search, brand)
        cars = Car.get_cars(search, brand)
        context = {
            "brands" : brands,
            "cars" : cars,
            "search_value" : search,
            "sel_brand" : brand,
        }
        return render(request, "cars.html", context)
    
    return render(request, "cars.html", {"brands": brands})
        
def new_car_view(request):
    new_car_form = CarForm()
    context = {
        'car_form' : new_car_form,
    }
    return render(request, "new_car.html", context)