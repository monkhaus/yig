from rest_framework import mixins
from rest_framework import viewsets, status
from api.models.extended_user import ExtendedUserModel
from api.serializers.extended_user import ExtendedUserSerializer
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCaptureRequest
import json
from rest_framework.response import Response

from django.conf import settings


class HandlePaymentsViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = ExtendedUserModel.objects.all()
    serializer_class = ExtendedUserSerializer


    def create(self, request):
        data = json.loads(request.data['body'])
        order_id = data['order_id']
        environment = SandboxEnvironment(client_id=settings.PAYPAL_API_KEY_PUBLISHABLE, client_secret=settings.PAYPAL_API_KEY_HIDDEN)
        client = PayPalHttpClient(environment)

        request = OrdersCaptureRequest(order_id)
        response = client.execute(request)

        if response.result.status == 'COMPLETED':
            extended_user, created = ExtendedUserModel.objects.get_or_create(user=self.request.user)
            extended_user.isPremium = True
            extended_user.save()
            return Response(status.HTTP_201_CREATED)
        else:
            # maybe just return response.result.status
            return Response(status.HTTP_402_PAYMENT_REQUIRED)
            


