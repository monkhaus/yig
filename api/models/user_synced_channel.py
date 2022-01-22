from unittest.util import _MAX_LENGTH
from django.db import models 
from django.contrib.auth import get_user_model
from .channel import Channel

class UserSyncedChannel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    channels = models.ManyToManyField(Channel, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.user)