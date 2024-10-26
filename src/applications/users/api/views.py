from rest_framework import mixins, status
from rest_framework.decorators import action

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drf_spectacular.utils import extend_schema

from applications.api.exceptions import BaseServiceException, handle_service_exception
from applications.users.api.serializers import (RetrieveUserSerializer, CreateUserSerializer, UpdateUserSerializer, \
 \
                                                UpdateUserGroupsSerializer, RetrieveUserAchievementSerializer,
                                                CreateUserAchievementSerializer, \
                                                UpdateUserAchievementSerializer)
from applications.users.models import User, UserAchievement
from applications.users.services import create_user, update_user, add_user_groups, delete_user_groups, \
    create_user_achievement, update_user_achievement

USERS_TAG = 'Пользователи'
USER_ACHIEVEMENT_TAG = 'Достижения пользователя'


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
            status.HTTP_201_CREATED: RetrieveUserSerializer,
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
            status.HTTP_200_OK: RetrieveUserSerializer,
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

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "No content",
        },
        tags=[USERS_TAG],
    )
    def destroy(self, request: Request, *args, **kwargs):
        user = self.get_object()
        try:
            user.delete()
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveUserSerializer,
        },
        tags=[USERS_TAG],
        request=UpdateUserGroupsSerializer,
    )
    @action(detail=True, methods=['PATCH'], url_path='add_groups')
    def add_groups(self, request: Request, *args, **kwargs):
        serializer = UpdateUserGroupsSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        try:
            user = add_user_groups(
                request.user,
                self.get_object(),
                **serializer.validated_data
            )
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(
            data=self.get_serializer(user).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveUserSerializer,
        },
        tags=[USERS_TAG],
        request=UpdateUserGroupsSerializer,
    )
    @action(detail=True, methods=['PATCH'], url_path='delete_groups')
    def delete_groups(self, request: Request, *args, **kwargs):
        serializer = UpdateUserGroupsSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        try:
            user = delete_user_groups(
                request.user,
                self.get_object(),
                **serializer.validated_data
            )
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(
            data=self.get_serializer(user).data,
            status=status.HTTP_200_OK,
        )


class UserAchievementViewSet(mixins.RetrieveModelMixin,
                             mixins.ListModelMixin,
                             GenericViewSet):
    queryset = UserAchievement.objects.all()
    serializer_class = RetrieveUserAchievementSerializer
    permission_classes = []

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveUserAchievementSerializer,
        },
        tags=[USER_ACHIEVEMENT_TAG],
    )
    def retrieve(self, request: Request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveUserAchievementSerializer(many=True),
        },
        tags=[USER_ACHIEVEMENT_TAG],
    )
    def list(self, request: Request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_201_CREATED: RetrieveUserAchievementSerializer,
        },
        tags=[USER_ACHIEVEMENT_TAG],
        request=CreateUserAchievementSerializer,
    )
    def create(self, request: Request, *args, **kwargs):
        serializer = CreateUserAchievementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user_achievement = create_user_achievement(**serializer.validated_data)
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(
            data=self.get_serializer(user_achievement).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveUserAchievementSerializer,
        },
        tags=[USER_ACHIEVEMENT_TAG],
        request=UpdateUserSerializer,
    )
    def partial_update(self, request: Request, *args, **kwargs):
        serializer = UpdateUserAchievementSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        try:
            user_achievement = update_user_achievement(
                self.get_object(),
                **serializer.validated_data
            )
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(
            data=self.get_serializer(user_achievement).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "No content",
        },
        tags=[USER_ACHIEVEMENT_TAG],
    )
    def destroy(self, request: Request, *args, **kwargs):
        user_achievement = self.get_object()
        try:
            user_achievement.delete()
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(status=status.HTTP_204_NO_CONTENT)
