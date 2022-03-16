from api.views.idea_generator import IdeaGeneratorViewSet
from api.views.sync_channel import SyncChannelViewSet
from api.views.video import VideoViewSet
from api.views.handle_payments import HandlePaymentsViewSet

__all__ = [
    'IdeaGeneratorViewSet',
    'HandlePaymentsViewSet',
    'SyncChannelViewSet',
    'VideoViewSet',
]