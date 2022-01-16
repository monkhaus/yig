from api.models.user_synced_channel import UserSyncedChannel
from rest_framework import serializers

from .channel import ChannelSerializer


class UserSyncedChannelSerializer(serializers.ModelSerializer):
	channels = ChannelSerializer(many=True)

	class Meta:
		model = UserSyncedChannel
		fields = ('id', 'user', 'channels')
