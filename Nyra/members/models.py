from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_profile",
    )
    biography = models.TextField(
        blank=True,
        null=True,
        default="Hello there. I am using Nyra!",
        max_length=256,
    )
