import json
from random import choice

from api.models.channel import Channel
from api.models.video import Video
from api.serializers.video import VideoSerializer
from django.contrib.auth.models import User
from rest_framework import status, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models.user_synced_channel import UserSyncedChannel
from api.models.extended_user import ExtendedUserModel
from rest_framework.exceptions import ValidationError


class IdeaGeneratorViewSet(viewsets.ModelViewSet):
    """This is only to generate a random video from my db."""
    ## permission_classes = (IsAuthenticated,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    DEFAULT_NUMBER_OF_VIDS = 2
    SYNCED = 'SYNCED'
    RANDOM = 'RANDOM'
    RAN_SYNC = 'RAN_SYNC'

    def get_queryset(self):
        """
        Return a video idea.
        """
        video_quantity = self.request.GET['video_quantity']
        generate_from = self.request.GET['generate_from']
        vid_quantity_dict = {
            'ONE': 1,
            'TWO': 2,
            'THREE': 3,
            'FOUR': 4
        }
        generate_from_dict = {
            'SYNCED': self.SYNCED,
            'RANDOM': self.RANDOM,
            'RAN_SYNC': self.RAN_SYNC,
        }

        video_quantity = (
            vid_quantity_dict[video_quantity]
            if video_quantity in vid_quantity_dict
            else self.DEFAULT_NUMBER_OF_VIDS
        )

        generate_from = (
            generate_from_dict[generate_from]
            if generate_from in generate_from_dict
            else self.DEFAULT_NUMBER_OF_VIDS
        )

        list_of_videos_to_return = []
        if generate_from == self.SYNCED:
            synced_channels = Channel.objects.filter(usersyncedchannel__user=self.request.user).values_list('id', flat=True)
            for video in range(video_quantity):
                videos = Video.objects.filter(channel_url_id__in=synced_channels)
                list_of_videos_to_return.append(choice(videos))
        elif generate_from == self.RANDOM:
            for video in range(video_quantity):
                videos = Video.objects.all()
                list_of_videos_to_return.append(choice(videos))
        elif generate_from == self.RAN_SYNC:
            number_of_random_vids = video_quantity // 2
            synced_channels = Channel.objects.filter(usersyncedchannel__user=self.request.user).values_list('id', flat=True)
            for video in range(video_quantity - number_of_random_vids):
                videos = Video.objects.filter(channel_url_id__in=synced_channels)
                list_of_videos_to_return.append(choice(videos))
            if number_of_random_vids:
                for video in range(number_of_random_vids):
                    videos = Video.objects.exclude(channel_url_id__in=synced_channels)
                    list_of_videos_to_return.append(choice(videos))

        
        try:
            extended_user = ExtendedUserModel.objects.get(user=self.request.user)
            if extended_user.isPremium:
                return list_of_videos_to_return
            else:
                raise ValidationError({'message': status.HTTP_402_PAYMENT_REQUIRED})
        except:
            raise ValidationError({'message': status.HTTP_402_PAYMENT_REQUIRED})
