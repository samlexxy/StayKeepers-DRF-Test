from .views import *
from django.urls import path, include

urlpatterns = [
    path('units/', ReservationView.as_view()),
]
