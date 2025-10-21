from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BookingViewSet)


urlpatterns = [
    path('stats/', BookingStatsView.as_view(), name='booking_stats')
]

urlpatterns += router.urls
