from django.contrib import admin
from api.models import Channel, UserSyncedChannel, Video

# Register your models here.
admin.site.register(Channel)
admin.site.register(UserSyncedChannel)
admin.site.register(Video)