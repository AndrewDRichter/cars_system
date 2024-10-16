from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def register_view(request):
    user_form = UserCreationForm()
    context = {
        'user_form' : user_form,
    }
    return render(request, "register.html", context)