import json
import random
import re

import requests
import scrapetube
from api.models.channel import Channel
from api.models.user_synced_channel import UserSyncedChannel
from api.models.video import Video
from api.serializers import ChannelSerializer, UserSyncedChannelSerializer
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class SyncChannelViewSet(viewsets.ModelViewSet):
    ## permission_classes = (IsAuthenticated,)
    queryset = UserSyncedChannel.objects.all()
    serializer_class = UserSyncedChannelSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request):
        """Sync channel with db and user"""
        channel, created = Channel.objects.get_or_create(channel_url=request.data.get('channel_url'))

        # if the channel has only just be created we need to get some extra info for the channel.
        if created:
            channel_soup = BeautifulSoup(requests.get(request.data.get('channel_url'),cookies={'CONSENT': 'YES+1'}).text,"html.parser")

            channel_data = re.search(r"var ytInitialData = ({.*});", str(channel_soup.prettify())).group(1)
            channel_data_json = json.loads(channel_data)

            channel_id = channel_data_json['header']['c4TabbedHeaderRenderer']['channelId']
            channel_name = channel_data_json['header']['c4TabbedHeaderRenderer']['title']
            channel_logo = channel_data_json['header']['c4TabbedHeaderRenderer']['avatar']['thumbnails'][2]['url']

            if channel:
                channel.channel_id = channel_id
                channel.channel_name = channel_name
                channel.channel_logo = channel_logo
                channel.save()
        try:
            synced_channel, created = UserSyncedChannel.objects.get_or_create(user=request.user)
            synced_channel.channels.add(channel)
        except:
            pass

        videos = list(scrapetube.get_channel(channel.channel_id))

        stored_videos = Video.objects.filter(channel_url=channel.id).values_list('youtube_video_id', flat=True)

        video_objects = []
        for video in videos:
            if video['videoId'] not in stored_videos:
                video_objects.append(Video(
                    channel_url=channel,
                    youtube_video_id=video['videoId'],
                    title= video['title']['runs'][0]['text'], 
                    thumbnail_url= video['thumbnail']['thumbnails'][3]['url'],
                    view_count= int(video['viewCountText']['simpleText'].replace(',', '').replace('views', '').strip())
                ))

        if video_objects:
            Video.objects.bulk_create(video_objects)

        return Response(status.HTTP_201_CREATED)
