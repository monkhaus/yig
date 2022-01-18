from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import scrapetube
from django.contrib.auth.models import User
from api.models.user_synced_channel import UserSyncedChannel
from api.models.channel import Channel
from api.models.video import Video
from api.serializers import UserSyncedChannelSerializer, ChannelSerializer

from rest_framework.response import Response
from rest_framework import status
import json
import random



class SyncChannelViewSet(viewsets.ModelViewSet):
    ## permission_classes = (IsAuthenticated,)
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def get_queryset(self):
        return self.queryset

    def create(self, request):
        """
        Sync channel with db and user
        """
        
        channel  = Channel.objects.get_or_create(channel_url="UCNajC7dxZrjTw4lBWWJYZ8w")
        videos = list(scrapetube.get_channel(channel[0].channel_url))

        video_objects = []
        for video in videos:
           video_objects.append(Video(
                channel_url=channel[0],
                title= video['title']['runs'][0]['text'], 
                thumbnail_url= video['thumbnail']['thumbnails'][0]['url'],
                view_count= int(video['viewCountText']['simpleText'].replace(',', '').replace('views', '').strip())
            ))

        import pdb; pdb.set_trace()

        Video.objects.bulk_create(video_objects)

        return Response(status.HTTP_201_CREATED)