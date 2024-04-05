from rest_framework import serializers

from applications.events.api.serializers import RetrieveEventSerializer
from applications.notifications.enums import NotificationState


class RetrieveNotificationStateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    state = serializers.ChoiceField(choices=NotificationState.choices)


class RetrieveNotificationSerializer(serializers.Serializer):
    state = serializers.IntegerField()
    time = serializers.DateTimeField()
    event = RetrieveEventSerializer()
    description = serializers.CharField()
