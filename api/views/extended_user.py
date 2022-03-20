from rest_framework import viewsets
from rest_framework.response import Response
from api.models.extended_user import ExtendedUserModel
from api.serializers.extended_user import ExtendedUserSerializer

class ExtendedUserViewSet(viewsets.ModelViewSet):
    queryset = ExtendedUserModel.objects.all()
    serializer_class = ExtendedUserSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)