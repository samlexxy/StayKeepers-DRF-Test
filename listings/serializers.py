from rest_framework import serializers
from .models import *

class ReservationSerializer(serializers.ModelSerializer):
    listing_type = serializers.ReadOnlyField(source="booking.listing.listing_type")
    title = serializers.ReadOnlyField(source="booking.hotel_room_type.title")
    country = serializers.ReadOnlyField(source="booking.listing.country")
    city = serializers.ReadOnlyField(source="booking.listing.city")
    price = serializers.ReadOnlyField(source="booking.price")
    class Meta:
        model = Reservation
        fields = ["listing_type", "title", "country", "city", "price"]


