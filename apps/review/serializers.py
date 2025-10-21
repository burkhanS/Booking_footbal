from rest_framework import serializers
from .models import Review, Favorite


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'user', 'stadium', 'rating', 'comment']



class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'stadium']
