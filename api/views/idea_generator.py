from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import scrapetube
from django.contrib.auth.models import User
from api.models.idea_generator import Generator
from api.serializers import IdeaGeneratorSerializer
from rest_framework.response import Response
from rest_framework import status
import json
import random


class IdeaGeneratorViewSet(viewsets.ModelViewSet):
    ## permission_classes = (IsAuthenticated,)
    queryset = Generator.objects.all()
    serializer_class = IdeaGeneratorSerializer

    def get_queryset(self):
        """
        Return a video idea.
        """

        videos = list(scrapetube.get_channel("UCNajC7dxZrjTw4lBWWJYZ8w"))

        video = random.choice(videos)
        

        vid_dict = {
            'title': video['title']['runs'][0]['text'], 
            'url': video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'],
            'view_count': [int(s) for s in video['viewCountText']['simpleText'].split() if s.isdigit()]
        }

        Generator.objects.create(
            title=vid_dict['title'],
            url=vid_dict['url'],
            view_count=vid_dict['view_count'][0]
        )

        return self.queryset