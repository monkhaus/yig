from rest_framework import serializers
from api.models.video import Video


class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = ('id', 'channel_url', 'title', 'thumbnail_url', 'view_count')