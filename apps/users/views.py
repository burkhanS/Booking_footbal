import random
from rest_framework import viewsets, generics, status
from .serializers import UsersSerializer, RegisterSerializer, VerifyOTPSerializer, SendOTPSerializer
from core.permissions import IsOwnerOrAdmin
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.core.cache import cache
import uuid

# Create your views here.
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsOwnerOrAdmin]



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        key = request.data.get('key')
        if not key:
            return Response({"error": "Не найден OTP ключ. Сначала подтвердите номер или email"}, status=status.HTTP_400_BAD_REQUEST)
        contact = cache.get(f"verified_{key}")
        if not contact:
            return Response({"error": "Неверный или просроченный ключ. Пройдите OTP проверку снова"}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        user = User.objects.get(id=response.data['id'])
        refresh = RefreshToken.for_user(user)
        response.data['tokens'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        cache.delete(f"verified_{key}")
        return response


class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class SendOTPView(APIView):
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.validated_data['contact']
        otp = str(random.randint(100000, 999999))
        cache.set(contact, otp, timeout=300)

        print(f"OTP for {contact}: {otp}")
        return Response({"message": "OTP отправлен"}, status=status.HTTP_200_OK)


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.validated_data['contact']
        otp_input = serializer.validated_data['otp']

        otp_stored = cache.get(f"otp_{contact}")
        if otp_stored is None:
            return Response({"error": "Срок OTP истек"}, status=status.HTTP_400_BAD_REQUEST)
        if otp_stored != otp_input:
            return Response({"error": "Неверный OTP"}, status=status.HTTP_400_BAD_REQUEST)
        key = str(uuid.uuid4())
        cache.set(f"verified_{key}", contact, timeout=900)
        cache.delete(f"otp_{contact}")
        return Response({"message": "OTP подтвержден", "key": key}, status=status.HTTP_200_OK)











