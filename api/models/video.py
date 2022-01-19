from django.db import models
from api.models.channel import Channel


class Video(models.Model):
    channel_url = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    youtube_video_id = models.CharField(max_length=256)
    title = models.CharField(max_length=250, null=True)
    thumbnail_url = models.URLField(null=True)
    view_count = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.title
