from asyncore import read
from rest_framework import serializers
from api.models.idea_generator import Generator


class IdeaGeneratorSerializer(serializers.ModelSerializer):
	channel_url = serializers.URLField(source='channel_url.channel_url', read_only=True)
	class Meta:
		model = Generator
		fields = ('id', 'title', 'url', 'view_count', 'channel_url')