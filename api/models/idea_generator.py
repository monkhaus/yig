from django.db import models
from django.utils import timezone


class Generator(models.Model):
    title = models.CharField(max_length=250, null=True)
    url = models.URLField(null=True)
    view_count = models.IntegerField(null=True)