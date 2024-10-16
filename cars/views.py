from django.shortcuts import render, redirect
from .models import Car, Brand
from .forms import CarModelForm

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
    context = {}
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        context['car_form'] = new_car_form
    if request.method == 'GET':
        new_car_form = CarModelForm()
        context['car_form'] = new_car_form
    return render(request, "new_car.html", context)