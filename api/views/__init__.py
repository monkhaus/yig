from api.views.idea_generator import IdeaGeneratorViewSet
from api.views.sync_channel import SyncChannelViewSet
from api.views.video import VideoViewSet
from api.views.handle_payments import HandlePaymentsViewSet
from api.views.extended_user import ExtendedUserViewSet

__all__ = [
    'ExtendedUserViewSet',
    'IdeaGeneratorViewSet',
    'HandlePaymentsViewSet',
    'SyncChannelViewSet',
    'VideoViewSet',
]