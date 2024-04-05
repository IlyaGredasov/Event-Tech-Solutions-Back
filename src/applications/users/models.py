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
        null=True
    )
    avatar = models.ImageField(
        null=True
    )
    vk = models.CharField(
        max_length=64,
        null=True
    )
    telegram = models.CharField(
        max_length=64,
        null=True
    )
    mail = models.CharField(
        max_length=64,
        null=True
    )
    phone_number = models.CharField(
        max_length=12,
        null=True,
        unique=True
    )
