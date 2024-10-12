from django.shortcuts import render
from .models import Car, Brand

def cars_view(request):
    brands = Brand.objects.all()
    if request.method == 'POST':
        search = request.POST.get("search_input", None)
        brand = request.POST.get("brand_select", None)
        obj = Car.get_cars(search, brand)
        context = {
            "brands" : brands,
            "search" : obj,
            "search_value" : search,
            "sel_brand" : brand,
        }
        return render(request, "cars.html", context)
    
    return render(request, "cars.html", {"brands": brands})
        