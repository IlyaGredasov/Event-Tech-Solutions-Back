from django.db import models


class EventParticipantState(models.IntegerChoices):
    REGISTERED = 0
    ARRIVED = 1
    SKIPPED = 2
    CANCELED = 3


