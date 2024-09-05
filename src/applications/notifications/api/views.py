from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from applications.api.exceptions import BaseServiceException, handle_service_exception
from applications.notifications.api.serializers import RetrieveNotificationSerializer, CreateNotificationSerializer, \
    UpdateNotificationSerializer
from applications.notifications.models import Notification
from applications.notifications.services import create_notification, update_notification

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

    @extend_schema(
        responses={
            status.HTTP_201_CREATED: RetrieveNotificationSerializer(),
        },
        tags=[NOTIFICATION_TAG],
        request=CreateNotificationSerializer,
    )
    def create(self, request, *args, **kwargs):
        serializer = CreateNotificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            notification = create_notification(request.user, **serializer.validated_data)
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(
            data=self.get_serializer(notification).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        request=UpdateNotificationSerializer,
        responses={
            status.HTTP_200_OK: RetrieveNotificationSerializer,
        },
        tags=[NOTIFICATION_TAG],
    )
    def partial_update(self, request: Request, *args, **kwargs):
        serializer = UpdateNotificationSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        try:
            notification = update_notification(
                self.get_object(),
                request.user,
                **serializer.validated_data
            )
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(
            data=self.get_serializer(notification).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "No content",
        },
        tags=[NOTIFICATION_TAG],
    )
    def destroy(self, request: Request, *args, **kwargs):
        notification = self.get_object()
        try:
            notification.delete()
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(status=status.HTTP_204_NO_CONTENT)
