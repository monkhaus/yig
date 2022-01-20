import json
from random import choice

import scrapetube
from api.models.channel import Channel
from api.models.idea_generator import Generator
from api.models.video import Video
from api.serializers import IdeaGeneratorSerializer
from api.serializers.channel import ChannelSerializer
from api.serializers.video import VideoSerializer
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class IdeaGeneratorViewSet(viewsets.ModelViewSet):
    """This is only to generate a random video from my db."""
    ## permission_classes = (IsAuthenticated,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        """
        Return a video idea.
        """
        random_video = choice(self.queryset)
        random_video_1 = choice(self.queryset)

        return [random_video, random_video_1]
