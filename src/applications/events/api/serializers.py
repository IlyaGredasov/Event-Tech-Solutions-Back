import datetime

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from applications.events.enums import EventParticipantState
from applications.events.models import EventParticipant
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


class RetrieveShortEventSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    place = serializers.CharField()
    time_start = serializers.DateTimeField()
    time_end = serializers.DateTimeField()
    image = serializers.ImageField()
    type = RetrieveEventTypeSerializer(read_only=True, many=True)


class RetrieveEventSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    state = RetrieveEventTypeSerializer(read_only=True)
    place = serializers.CharField()
    time_start = serializers.DateTimeField()
    time_end = serializers.DateTimeField()
    duration = serializers.SerializerMethodField(method_name="get_duration")
    is_upcoming = serializers.SerializerMethodField(method_name="get_is_upcoming")
    user_state = serializers.SerializerMethodField(method_name="get_user_state")
    reference = serializers.CharField()
    reference_video = serializers.CharField()
    type = RetrieveEventTypeSerializer(read_only=True, many=True)
    speaker = RetrieveRelatedUserSerializer(read_only=True)
    managers = RetrieveRelatedUserSerializer(
        many=True,
        read_only=True,
    )
    participants = RetrieveRelatedUserSerializer(many=True, read_only=True)
    image = serializers.ImageField()

    @extend_schema_field(OpenApiTypes.INT)
    def get_user_state(self, obj):
        participants = EventParticipant.objects.filter(event=obj, user=self.context["request"].user)
        state = list(participants.values_list("state", flat=True))
        if len(state) == 0:
            return None
        else:
            return state[0]

    @extend_schema_field(OpenApiTypes.JSON_PTR)
    def get_duration(self, obj):
        time = (obj.time_end - obj.time_start).total_seconds()
        return {"hours": time // 3600, "minutes": (time % 3600) // 60, "seconds": time % 60}

    @extend_schema_field(OpenApiTypes.BOOL)
    def get_is_upcoming(self, obj):
        return obj.time_end.timestamp() >= datetime.datetime.now().timestamp()
