from rest_framework import mixins, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drf_spectacular.utils import extend_schema

from applications.api.exceptions import BaseServiceException, handle_service_exception
from applications.users.api.serializers import RetrieveUserSerializer, CreateUserSerializer, UpdateUserSerializer
from applications.users.models import User
from applications.users.services import create_user, update_user

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

    @extend_schema(
        responses={
            status.HTTP_201_CREATED: RetrieveUserSerializer(),
        },
        tags=[USERS_TAG],
        request=CreateUserSerializer,
    )
    def create(self, request: Request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = create_user(**serializer.validated_data)
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(
            data=self.get_serializer(user).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        responses={
            status.HTTP_201_CREATED: RetrieveUserSerializer(),
        },
        tags=[USERS_TAG],
        request=UpdateUserSerializer,
    )
    def partial_update(self, request: Request, *args, **kwargs):
        serializer = UpdateUserSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        try:
            user = update_user(
                self.get_object(),
                **serializer.validated_data
            )
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(
            data=self.get_serializer(user).data,
            status=status.HTTP_200_OK,
        )
