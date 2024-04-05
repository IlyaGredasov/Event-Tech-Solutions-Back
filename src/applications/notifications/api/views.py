from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets

from applications.notifications.api.serializers import RetrieveNotificationSerializer
from applications.notifications.models import Notification

NOTIFICATION_TAG = 'Уведомления'


class NotificationViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = RetrieveNotificationSerializer
    queryset = Notification.objects.all()

    def get_queryset(self):
        return super().get_queryset()

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveNotificationSerializer,
        },
        tags=[NOTIFICATION_TAG],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveNotificationSerializer(many=True),
        },
        tags=[NOTIFICATION_TAG],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
