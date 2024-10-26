from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models


class User(AbstractUser):
    username_validator = ASCIIUsernameValidator
    username = models.CharField(
        max_length=64,
        unique=True,
        validators=[username_validator],
    )
    job = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )
    avatar = models.ImageField(
        upload_to='users/%Y/%m/%d',
        null=True,
        blank=True
    )
    vk = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )
    telegram = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )
    mail = models.CharField(
        max_length=64,
        null=True,
        blank=True
    )
    phone_number = PhoneNumberField(
        unique=True,
        null=True,
        blank=True
    )
    score = models.IntegerField(
        default=0,
    )


class UserAchievement(models.Model):
    from applications.events.models import EventType
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='achievements',
    )
    achievement_type = models.ForeignKey(
        to=EventType,
        on_delete=models.CASCADE,
    )
    score = models.IntegerField()
    achievement_time = models.DateField(auto_now=True)
