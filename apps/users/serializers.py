from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'first_name', 'last_name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password', 'password2', 'is_owner']
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'Password': 'Пароли не совпадают'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        user.is_active = False
        user.save()


class SendOTPSerializer(serializers.Serializer):
    contact = serializers.CharField(max_length=100)


class VerifyOTPSerializer(serializers.Serializer):
    contact = serializers.CharField(max_length=100)
    otp = serializers.CharField(max_length=6)
