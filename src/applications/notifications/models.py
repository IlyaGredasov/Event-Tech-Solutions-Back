from django.db import models
from applications.notifications.enums import NotificationState
from applications.users.models import User
from applications.events.models import Event


class Notification(models.Model):
    state = models.IntegerField(choices=NotificationState.choices)
    time = models.DateTimeField()
    event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE,
        related_name='event_notifications',
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_notifications',
    )
    description = models.TextField(
        max_length=255,
    )
