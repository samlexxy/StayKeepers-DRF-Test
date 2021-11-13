from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from rest_framework.filters import OrderingFilter

class BookFilter(filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="booking__price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="booking__price", lookup_expr="lte")
    check_in = filters.DateFilter(lookup_expr="gte")
    check_out = filters.DateFilter(lookup_expr="lte")

    class Meta:
        model = Reservation
        fields = [
        #     "min_price",
            "max_price",
            "check_in",
            "check_out",
        ]

class ReservationView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = BookFilter
    ordering = ['booking__price']
