from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'stadiums', StadiumViewSet)
router.register(r'stadium_images', StadiumImageViewSet)

urlpatterns = router.urls