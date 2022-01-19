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
        """Sync channel with db and user"""
        channel, created = Channel.objects.get_or_create(channel_url=request.data.get('channel_url'))
        videos = list(scrapetube.get_channel(channel.channel_url))

        if not created:
            # grab all the records related to the channel url
            stored_videos = Video.objects.filter(channel_url=channel.id).values_list('youtube_video_id', flat=True)

        video_objects = []
        list_of_scraped_youtube_ids = []
        for video in videos:
            if video['videoId'] not in stored_videos:
                video_objects.append(Video(
                    channel_url=channel,
                    youtube_video_id=video['videoId'],
                    title= video['title']['runs'][0]['text'], 
                    thumbnail_url= video['thumbnail']['thumbnails'][0]['url'],
                    view_count= int(video['viewCountText']['simpleText'].replace(',', '').replace('views', '').strip())
                ))

        Video.objects.bulk_create(video_objects)

        return Response(status.HTTP_201_CREATED)