from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from applications.notifications.enums import NotificationState
from applications.users.models import User


class RetrieveGroupSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class RetrieveUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    avatar = serializers.ImageField()
    job = serializers.CharField()
    vk = serializers.CharField()
    telegram = serializers.CharField()
    mail = serializers.CharField()
    phone_number = serializers.CharField()
    groups = RetrieveGroupSerializer(many=True, read_only=True)


class RetrieveRelatedUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    avatar = serializers.ImageField()


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    job = serializers.CharField(max_length=255, required=False)
    avatar = serializers.ImageField(required=False)
    vk = serializers.CharField(max_length=255, required=False)
    telegram = serializers.CharField(max_length=255, required=False)
    mail = serializers.CharField(max_length=255, required=False)
    phone_number = serializers.CharField(max_length=255, required=False)


class UpdateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=False)
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    password = serializers.CharField(max_length=255, required=False)
    job = serializers.CharField(max_length=255, required=False)
    avatar = serializers.ImageField(required=False)
    vk = serializers.CharField(max_length=255, required=False)
    telegram = serializers.CharField(max_length=255, required=False)
    mail = serializers.CharField(max_length=255, required=False)
    phone_number = serializers.CharField(max_length=255, required=False)


class UpdateUserGroupsSerializer(serializers.Serializer):
    groups = serializers.ListField(
        child=PrimaryKeyRelatedField(
            queryset=Group.objects.all()
        )
    )


class UserNotificationSerializer(serializers.Serializer):
    state = serializers.ChoiceField(choices=NotificationState.choices)
    time = serializers.DateTimeField()
    event = serializers.CharField()
    user = serializers.CharField()
    description = serializers.CharField()


class RetrieveUserAchievementSerializer(serializers.Serializer):
    from applications.events.api.serializers import RetrieveEventTypeSerializer
    user = RetrieveRelatedUserSerializer(read_only=True)
    event_type = RetrieveEventTypeSerializer(read_only=True)
    score = serializers.IntegerField(default=0)
    achievement_time = serializers.DateTimeField()


class CreateUserAchievementSerializer(serializers.Serializer):
    from applications.events.models import EventType
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    event_type = serializers.PrimaryKeyRelatedField(
        queryset=EventType.objects.all()
    )


class UpdateUserAchievementSerializer(serializers.Serializer):
    from applications.events.api.serializers import RetrieveEventTypeSerializer
    user = RetrieveRelatedUserSerializer(read_only=True)
    event_type = RetrieveEventTypeSerializer(read_only=True)
    score = serializers.IntegerField(required=False)
    achievement_time = serializers.DateTimeField()
