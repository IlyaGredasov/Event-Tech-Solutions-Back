from django.db import models


class NotificationState(models.IntegerChoices):
    SENT = 0
    DELIVERED = 1
    READ = 2
