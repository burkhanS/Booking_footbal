from django.shortcuts import render
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrAdmin


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]



def get_queryset(self):
    user = self.request.user
    if user.is_staff:
        return Payment.objects.all
    return Payment.objects.filter(user=user)



