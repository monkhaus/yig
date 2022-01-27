from django.db import models
from django.utils import timezone


class Channel(models.Model):
    channel_url = models.URLField(unique=True, null=True)
    channel_id = models.CharField(max_length=255, unique=True, null=True)
    channel_name = models.CharField(max_length=255, null=True)
    channel_logo = models.URLField(null=True)
    channel_subscribers = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.channel_url
