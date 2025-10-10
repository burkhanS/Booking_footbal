from rest_framework import viewsets, permissions, filters
from .models import Stadium, StadiumImage
from .serializers import StadiumSerializer, StadiumImageSerializer
from core.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .filters import StadiumFilter

# Create your views here.


class StadiumViewSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = StadiumFilter


class StadiumImageViewSet(viewsets.ModelViewSet):
    queryset = StadiumImage.objects.all()
    serializer_class = StadiumImageSerializer