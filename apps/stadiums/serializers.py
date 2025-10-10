from rest_framework import serializers
from .models import Stadium, StadiumImage


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ['id', 'name', 'location', 'price_per_hour', 'size', 'type', 'description', 'owner', 'latitude', 'longitude']



class StadiumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumImage
        fields = ['id', 'stadium', 'image']


