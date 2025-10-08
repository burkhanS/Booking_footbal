from rest_framework import serializers
from .models import Review, Favorite


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'stadium', 'rating', 'comment']
        read_only_fields = ['id']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'stadium']
