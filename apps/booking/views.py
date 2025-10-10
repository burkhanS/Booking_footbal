from django.shortcuts import render
from django.utils import timezone
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import viewsets, filters, status
from core.permissions import IsOwnerOrAdmin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookingFilter
from rest_framework.decorators import action
from django.db.models import Count, Sum
from apps.payment.models import Payment
from rest_framework.permissions import IsAdminUser

# Create your views here.


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsOwnerOrAdmin]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookingFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(detail=False, methods=['get'], url_path='history')
    def history(self, request):
        now = timezone.now()
        bookings = Booking.objects.filter(user=self.request.user).order_by('-start_time')

        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'], url_path='admin_stats', permission_classes=[IsAdminUser])
    def admin_stats(self, request):
        total = Booking.objects.count()
        active = Booking.objects.filter(status='active').count()
        completed = Booking.objects.filter(status='completed').count()
        cancelled = Booking.objects.filter(status='cancelled').count()

        total_payments = Payment.objects.count()
        successful_payments = Payment.objects.filter(status='success').count()
        total_revenue = Payment.objects.filter(status='success').aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({
            "total_bookings": total,
            "active_bookings": active,
            "completed_bookings": completed,
            "cancelled_bookings": cancelled,
            "total_payments": total_payments,
            "successful_payments": successful_payments,
            "total_revenue": total_revenue,
        }, status=status.HTTP_200_OK)




