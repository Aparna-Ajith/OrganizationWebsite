# acts/urls.py

from django.urls import path
from acts import views

urlpatterns = [
    path("", views.acts_index, name="acts_index"),
    path("<int:pk>/", views.acts_detail, name="acts_detail"),
]
