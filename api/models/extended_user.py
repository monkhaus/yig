
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class ExtendedUserModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    isPremium = models.BooleanField(default=False)