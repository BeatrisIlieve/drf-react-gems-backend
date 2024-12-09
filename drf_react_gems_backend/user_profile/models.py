from django.db import models

from drf_react_gems_backend.user_credentials.models import (
    UserCredentials,
)


class UserProfile(models.Model):    
    user = models.OneToOneField(
        to=UserCredentials,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="user_profile",
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
    )
