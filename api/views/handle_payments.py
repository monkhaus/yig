from rest_framework import mixins
from rest_framework import viewsets
from api.models.extended_user import ExtendedUserModel
from api.serializers.extended_user import ExtendedUserSerializer
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCaptureRequest

from django.conf import settings


class HandlePaymentsViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = ExtendedUserModel.objects.all()
    serializer_class = ExtendedUserSerializer


    def create(self, request):
        import pdb; pdb.set_trace()
        order_id = data['order_id']
        environment = SandboxEnvironment(client_id=settings.PAYPAL_API_KEY_PUBLISHABLE, client_secret=settings.PAYPAL_API_KEY_HIDDEN)
        client = PayPalHttpClient(environment)

        request = OrdersCaptureRequest(order_id)
        response = client.execute(request)
