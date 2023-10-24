from django.shortcuts import render

# Create your views here.

# defining a view function named home that will render a HTML page called home:


def home(request):
    return render(request, "pages/home.html", {})
