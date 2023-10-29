# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render


def signup(request):
    return render(request, "templates/registration/signup.html", {})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    # signup(request)
   # return render(request, "templates/registration/signup.html", context)
