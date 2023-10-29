# pages/urls.py

from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("", views.login, name='accounts/login'),
    path("contact/", views.contact, name='contact')
]
