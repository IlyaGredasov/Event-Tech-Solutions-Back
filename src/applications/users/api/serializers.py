from rest_framework import serializers

from applications.notifications.enums import NotificationState


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
    password = serializers.CharField(max_length=255)
    job = serializers.CharField(max_length=255)
    avatar = serializers.ImageField(required=False)
    vk = serializers.CharField(max_length=255, required=False)
    telegram = serializers.CharField(max_length=255, required=False)
    mail = serializers.CharField(max_length=255, required=False)
    phone_number = serializers.CharField(max_length=255, required=False)


class UpdateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=False)
    password = serializers.CharField(max_length=255, required=False)
    job = serializers.CharField(max_length=255, required=False)
    avatar = serializers.ImageField(required=False)
    vk = serializers.CharField(max_length=255, required=False)
    telegram = serializers.CharField(max_length=255, required=False)
    mail = serializers.CharField(max_length=255, required=False)
    phone_number = serializers.CharField(max_length=255, required=False)


class UserNotificationSerializer(serializers.Serializer):
    state = serializers.ChoiceField(choices=NotificationState.choices)
    time = serializers.DateTimeField()
    event = serializers.CharField()
    user = serializers.CharField()
    description = serializers.CharField()
