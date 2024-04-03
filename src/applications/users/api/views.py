from rest_framework import mixins, status
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet

from drf_spectacular.utils import extend_schema

from applications.users.api.serializers import RetrieveUserSerializer
from applications.users.models import User


USERS_TAG = 'Пользователи'


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RetrieveUserSerializer
    permission_classes = []

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveUserSerializer,
        },
        tags=[USERS_TAG],
    )
    def retrieve(self, request: Request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveUserSerializer(many=True),
        },
        tags=[USERS_TAG],
    )
    def list(self, request: Request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
