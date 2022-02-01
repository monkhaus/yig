from api.models.video import Video
from api.serializers import VideoSerializer
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class VideoViewSet(viewsets.ModelViewSet):
    """
    viewset for collection really. load specific videos that have been saved by user 
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        return self.queryset.filter(users=self.request.user)
    
    def create(self, request):
        video = Video.objects.get(id=request.data['id'])
        video.users.add(request.user.id)
        return Response(status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        video = Video.objects.get(id=pk)
        video.users.remove(request.user.id)
        return Response(status.HTTP_200_OK)