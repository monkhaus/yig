from django.urls import path, include
from .views import (
    IdeaGeneratorViewSet,
    SyncChannelViewSet
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'generator', IdeaGeneratorViewSet)
router.register(r'sync', SyncChannelViewSet)

urlpatterns = router.urls