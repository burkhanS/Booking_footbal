from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)
router.register(r'favorites', FavoriteViewSet)

urlpatterns = router.urls