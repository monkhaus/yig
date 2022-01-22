from django.contrib import admin
from api.models import Channel, UserSyncedChannel, Video



class ChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_name', 'channel_id', 'channel_url')

# Register your models here.
admin.site.register(Channel, ChannelAdmin)
admin.site.register(UserSyncedChannel)
admin.site.register(Video)