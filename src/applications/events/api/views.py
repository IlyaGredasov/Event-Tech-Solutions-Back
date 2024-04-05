from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from django_filters import rest_framework as filters

from applications.api.exceptions import BaseServiceException, handle_service_exception
from applications.api.views import CustomUpdateModelMixin
from applications.events.api.serializers import (RetrieveEventParticipantSerializer, RetrieveEventSerializer,
                                                 UpdateEventParticipantSerializer)
from applications.events.models import Event, EventParticipant
from applications.events.services import create_event_participant, update_event_participant

EVENTS_TAG = 'Мероприятия'
EVENT_PARTICIPANTS_TAG = 'Участники мероприятия'


class EventFilter(filters.FilterSet):
    time_start__gte = filters.DateTimeFilter(field_name='start_time', lookup_expr='gte')
    time_start__lte = filters.DateTimeFilter(field_name='start_time', lookup_expr='lte')
    class Meta:
        model = Event
        fields = ['type', 'time_start']


class EventViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = RetrieveEventSerializer
    queryset = Event.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter

    def get_queryset(self):
        self.queryset = self.queryset.filter_visible_for(
            self.request.user,
        ).select_related(
            'speaker',
        ).prefetch_related(
            'managers',
        )
        return super().get_queryset()

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveEventSerializer,
        },
        tags=[EVENTS_TAG],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveEventSerializer(many=True),
        },
        tags=[EVENTS_TAG],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class EventParticipantViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.CreateModelMixin,
                              CustomUpdateModelMixin,
                              viewsets.GenericViewSet):
    queryset = EventParticipant.objects.all()
    serializer_class = RetrieveEventParticipantSerializer

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        event_pk = kwargs.get('event_pk')
        if event_pk:
            self.event = get_object_or_404(Event.objects.all(), pk=event_pk)

    def get_queryset(self):
        self.queryset = self.queryset.filter(
            event=self.event,
        ).select_related(
            'event',
        )
        return super().get_queryset()

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveEventParticipantSerializer(many=True),
        },
        tags=[EVENT_PARTICIPANTS_TAG],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        responses={
            status.HTTP_200_OK: RetrieveEventParticipantSerializer,
        },
        tags=[EVENT_PARTICIPANTS_TAG],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, *kwargs)

    @extend_schema(
        responses={
            status.HTTP_201_CREATED: RetrieveEventParticipantSerializer,
        },
        request=None,
        tags=[EVENT_PARTICIPANTS_TAG],
    )
    def create(self, request: Request, *args, **kwargs):
        try:
            event_participant = create_event_participant(self.event, request.user)
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(
            data=self.get_serializer(event_participant).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(
        request=UpdateEventParticipantSerializer,
        responses={
            status.HTTP_200_OK: RetrieveEventParticipantSerializer,
        },
        tags=[EVENT_PARTICIPANTS_TAG],
    )
    def partial_update(self, request: Request, *args, **kwargs):
        serializer = UpdateEventParticipantSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        try:
            event_participant = update_event_participant(
                self.get_object(),
                request.user,
                **serializer.validated_data
            )
        except BaseServiceException as e:
            return handle_service_exception(e)
        return Response(
            data=self.get_serializer(event_participant).data,
            status=status.HTTP_200_OK,
        )
