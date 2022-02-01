from django.urls import path, include
from .views import (
    IdeaGeneratorViewSet,
    SyncChannelViewSet,
    VideoViewSet
)
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'generator', IdeaGeneratorViewSet)
router.register(r'sync', SyncChannelViewSet)
router.register(r'video', VideoViewSet)

urlpatterns = router.urls