from django.shortcuts import render
from rest_framework import viewsets
from .models import Review, Favorite
from .serializers import ReviewSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.permissions import IsFavoriteOwner


# Create your views here.


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsFavoriteOwner]