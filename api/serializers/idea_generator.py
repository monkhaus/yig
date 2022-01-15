from rest_framework import serializers
from api.models.idea_generator import Generator


class IdeaGeneratorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Generator
		fields = ('id', 'title', 'url', 'view_count')