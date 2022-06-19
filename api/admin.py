from django.contrib import admin
from api.models import Channel, UserSyncedChannel, Video
from api.models.extended_user import ExtendedUserModel



class ChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_name', 'channel_id', 'channel_url', 'channel_logo', 'channel_subscribers')

class ExtendedUserModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'isPremium')

# Register your models here.
admin.site.register(Channel, ChannelAdmin)
admin.site.register(UserSyncedChannel)
admin.site.register(Video)
admin.site.register(ExtendedUserModel, ExtendedUserModelAdmin)