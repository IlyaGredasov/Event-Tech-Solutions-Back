from rest_framework import serializers

from applications.events.enums import EventParticipantState
from applications.users.api.serializers import RetrieveRelatedUserSerializer


class RetrieveEventTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class RetrieveEventParticipantSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    state = serializers.CharField()
    user = RetrieveRelatedUserSerializer(read_only=True)


class UpdateEventParticipantSerializer(serializers.Serializer):
    state = serializers.ChoiceField(
        choices=EventParticipantState.choices,
    )


class RetrieveEventSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    state = RetrieveEventTypeSerializer(read_only=True)
    place = serializers.CharField()
    time_start = serializers.DateTimeField()
    time_end = serializers.DateTimeField()
    reference = serializers.CharField()
    reference_video = serializers.CharField()

    speaker = RetrieveRelatedUserSerializer(read_only=True)

    managers = RetrieveRelatedUserSerializer(
        many=True,
        read_only=True,
    )



