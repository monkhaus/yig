from django.db import models


class Generator(models.Model):
    title = models.CharField(max_length=250, null=True)
    url = models.URLField(null=True)
    thumbnail_url = models.URLField(null=True)
    view_count = models.IntegerField(null=True)