from django.shortcuts import render
from rest_framework import viewsets
from .models import Review, Favorite
from .serializers import ReviewSerializer, FavoriteSerializer
from core.permissions import IsFavoriteOwnerOrAdmin, IsReviewOwnerOrAdmin

# Create your views here.


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Review.objects.all()
        return Review.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsFavoriteOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Favorite.objects.all()
        return Favorite.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)