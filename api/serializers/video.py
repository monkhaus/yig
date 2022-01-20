from rest_framework import serializers
from api.models.video import Video


class VideoSerializer(serializers.ModelSerializer):
	channel_url = serializers.CharField(source='channel_url.channel_url', read_only=True)
	class Meta:
		model = Video
		fields = ('id', 'youtube_video_id', 'channel_url', 'title', 'thumbnail_url', 'view_count', 'channel_url')