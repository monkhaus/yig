from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import scrapetube
from django.contrib.auth.models import User
from api.models.user_synced_channel import UserSyncedChannel
from api.models.channel import Channel
from api.models.video import Video
from api.serializers import UserSynced

from rest_framework.response import Response
from rest_framework import status
import json
import random



class SyncChannelViewSet(viewsets.ModelViewSet):
    ## permission_classes = (IsAuthenticated,)
    queryset = UserSyncedChannel.objects.all()
    serializer_class = UserSyncedChannel

    def create(self, request):
        """
        Sync channel with db and user
        """
        channel  = Channel.objects.get_or_create(channel_url=request.data['channel'])
 

        if not channel:
            videos = list(scrapetube.get_channel("UCNajC7dxZrjTw4lBWWJYZ8w"))
           

            # video = random.choice(videos)

            video_objects = []
            for vid in videos:
                video_objects.append({
                    'title': video['title']['runs'][0]['text'], 
                    'url': video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'],
                    'thumbnail_url': video['thumbnail']['thumbnails'][0]['url'],
                    'view_count': int(video['viewCountText']['simpleText'].replace(',', '').replace('views', '').strip())
                })
        

        Video.objects.bulk_create()

        return self.queryset