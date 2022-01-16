from rest_framework import serializers
from api.models.channel import Channel

# I'm not sure if we need this as channels are going to be pulled from user_synced_channel
class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = ('id', 'channel')