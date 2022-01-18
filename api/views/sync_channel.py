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
        import pdb; pdb.set_trace()
        channel  = Channel.objects.get_or_create(channel_url=request.data['channel'])
 
        if not channel:
            videos = list(scrapetube.get_channel("UCNajC7dxZrjTw4lBWWJYZ8w"))

            video_objects = []
            for video in videos:
                video_objects.append({
                    'channel_url': channel.id,
                    'title': video['title']['runs'][0]['text'], 
                    'thumbnail_url': video['thumbnail']['thumbnails'][0]['url'],
                    'view_count': int(video['viewCountText']['simpleText'].replace(',', '').replace('views', '').strip())
                })

        Video.objects.bulk_create(**video_objects)

        return Response(status.HTTP_201_CREATED)