from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import viewsets, filters
from core.permissions import IsBookingOwnerOrAdmin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookingFilter
from django.db.models import Count, Avg
from rest_framework.permissions import IsAdminUser
# Create your views here.
from ..review.models import Review


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsBookingOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookingFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



# Статистика для админа

class BookingStatsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        stadium_ratings = (
            Review.objects.values('stadium__name')
            .annotate(avg_rating=Avg('rating'), total_reviews=Count('id'))
            .order_by('-avg_rating')
        )

        total_reviews = Review.objects.count()
        rating_counts = (
            Review.objects.values('rating')
            .annotate(count=Count('id'))
            .order_by('rating')
        )

        best = stadium_ratings.first()
        worst = stadium_ratings.last()

        data = {
            'total_reviews': total_reviews,
            'rating_counts': list(rating_counts),
            'stadium_ratings': list(stadium_ratings),
            'best_stadium': best,
            'worst_stadium': worst,
        }

        return Response(data)



