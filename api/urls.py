from django.urls import path, include

from api.views.handle_payments import HandlePaymentsViewSet
from .views import (
    IdeaGeneratorViewSet,
    SyncChannelViewSet,
    VideoViewSet,
    HandlePaymentsViewSet,
    ExtendedUserViewSet,
)
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'generator', IdeaGeneratorViewSet)
router.register(r'sync', SyncChannelViewSet)
router.register(r'video', VideoViewSet)
router.register(r'payment', HandlePaymentsViewSet)
router.register(r'me', ExtendedUserViewSet)

urlpatterns = router.urls