from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework import viewsets, status
from core.permissions import IsPaymentOwnerOrAdmin


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsPaymentOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            Payment.objects.all()
        return Payment.objects.filter(booking__user=self.request.user)

    def perform_create(self, serializer):
        booking = serializer.validated_data.get('booking')
        if booking.user != self.request.user:
            raise PermissionDenied('Вы не можете создать оплату')
        serializer.save()




