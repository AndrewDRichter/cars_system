from django.shortcuts import render
from .models import Car

def cars_view(request):
    if request.method == 'POST':
        search = request.POST.get("search_input", None)
        print(search)
        if search:
            obj = Car.get_cars(search)
        else:
            obj = Car.get_cars()
        return render(request, "cars.html", {'search': obj})
    
    return render(request, "cars.html")
        