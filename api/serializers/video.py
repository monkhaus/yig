from rest_framework import serializers
from api.models.video import Video
from api.serializers.user import UserSerializer

class VideoSerializer(serializers.ModelSerializer):
	channel_url = serializers.CharField(source='channel_url.channel_url', read_only=True)
	users = UserSerializer(many=True)

	class Meta:
		model = Video
		fields = ('id', 'youtube_video_id', 'channel_url', 'title', 'thumbnail_url', 'view_count', 'channel_url', 'users')