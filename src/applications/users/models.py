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
