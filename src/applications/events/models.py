from django.db import models
from django.db.models import Q, Exists, OuterRef

from applications.events.enums import EventParticipantState
from applications.users.models import User


class EventQuerySet(models.QuerySet):
    def filter_visible_for(self, actor: User):
        return self.filter(
            Q(author=actor) |
            (
                Exists(EventParticipant.objects.filter(event=OuterRef('id'), state=EventParticipantState.ARRIVED))
            ) |
            Q(managers=actor)
        )


class EventType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Event Type: {self.name} {self.id}"


class Event(models.Model):
    objects = EventQuerySet.as_manager()
    name = models.CharField(max_length=255)
    type = models.ForeignKey(
        EventType,
        on_delete=models.PROTECT,
        related_name='typed_events',
    )
    place = models.CharField(max_length=255)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    speaker = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='speaked_events',
    )
    reference = models.CharField(max_length=255)
    reference_video = models.CharField(max_length=255)
    author = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='authored_events',
    )
    managers = models.ManyToManyField(
        to=User,
        related_name='managed_events',
        blank=True,
    )
    participants = models.ManyToManyField(
        to=User,
        through='EventParticipant',
        related_name='events',
    )
    image = models.ImageField(upload_to='events/%Y/%m/%d', null=True, blank=True)
    is_online = models.BooleanField(default=False)
    description = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Event {self.id} {self.name} | {self.type}'


class EventParticipant(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='event_participation',
    )
    state = models.IntegerField(
        choices=EventParticipantState.choices,
        default=EventParticipantState.REGISTERED,
    )

    def __str__(self):
        return f'EventParticipant {self.id} | {self.user} | {self.event}'


class EventComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment',
        verbose_name_plural = 'Event comments'

    def __str__(self):
        return f'Comment {self.user} {self.event}'
