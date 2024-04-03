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
    avatar = models.ImageField(null=True)




