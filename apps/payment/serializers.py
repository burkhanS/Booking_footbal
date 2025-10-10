from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'amount', 'provider', 'status', 'transaction_id', 'created_at']
        read_only_fields = ['id', 'status', 'created_at', 'transaction_id']
