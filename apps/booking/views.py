from django.shortcuts import render
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import viewsets
from core.permissions import IsOwnerOrAdmin


# Create your views here.


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

