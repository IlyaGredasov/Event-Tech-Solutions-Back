from rest_framework import serializers

from applications.events.api.serializers import RetrieveEventSerializer
from applications.events.models import Event
from applications.notifications.enums import NotificationState
from applications.users.api.serializers import RetrieveUserSerializer
from applications.users.models import User


class RetrieveNotificationStateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    state = serializers.ChoiceField(choices=NotificationState.choices)


class RetrieveNotificationSerializer(serializers.Serializer):
    state = serializers.IntegerField()
    time = serializers.DateTimeField()
    event = RetrieveEventSerializer()
    user = RetrieveUserSerializer()
    description = serializers.CharField()


class CreateNotificationSerializer(serializers.Serializer):
    event = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )
    description = serializers.CharField()


class UpdateNotificationSerializer(serializers.Serializer):
    description = serializers.CharField(required=False)
