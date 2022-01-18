from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import scrapetube
from django.contrib.auth.models import User
from api.models.idea_generator import Generator
from api.models.channel import Channel
from api.serializers import IdeaGeneratorSerializer
from rest_framework.response import Response
from rest_framework import status
import json
import random

from api.serializers.channel import ChannelSerializer


class IdeaGeneratorViewSet(viewsets.ModelViewSet):
    ## permission_classes = (IsAuthenticated,)
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def get_queryset(self):
        """
        Return a video idea.
        """

        videos = list(scrapetube.get_channel("UCNajC7dxZrjTw4lBWWJYZ8w"))

        video = random.choice(videos)
        
        vid_dict = {
            'title': video['title']['runs'][0]['text'], 
            'url': video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'],
            'thumbnail_url': video['thumbnail']['thumbnails'][0]['url'],
            'view_count': int(video['viewCountText']['simpleText'].replace(',', '').replace('views', '').strip())
        }

        Generator.objects.create(
            title=vid_dict['title'],
            url=vid_dict['url'],
            thumbnail_url=vid_dict['thumbnail_url'],
            view_count=vid_dict['view_count']
        )

        return self.queryset