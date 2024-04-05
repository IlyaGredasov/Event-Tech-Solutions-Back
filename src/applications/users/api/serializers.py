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


class UserNotificationSerializer(serializers.Serializer):
    state = serializers.ChoiceField(choices=NotificationState.choices)
    time = serializers.DateTimeField()
    event = serializers.CharField()
    user = serializers.CharField()
    description = serializers.CharField()
