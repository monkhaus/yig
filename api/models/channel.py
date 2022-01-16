from django.db import models
from django.utils import timezone


class Channel(models.Model):
    channel_url = models.URLField(unique=True, null=True)

    def __str__(self) -> str:
        return self.channel_url