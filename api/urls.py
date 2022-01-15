from django.urls import path, include
from .views import (
    IdeaGeneratorViewSet
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'generator', IdeaGeneratorViewSet)

urlpatterns = router.urls