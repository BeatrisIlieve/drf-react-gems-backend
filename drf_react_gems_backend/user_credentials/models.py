from django.db import (
    models,
)

from django.contrib.auth.base_user import (
    AbstractBaseUser,
)
from django.contrib.auth.models import (
    PermissionsMixin,
)

from drf_react_gems_backend.user_credentials.managers import (
    UserCredentialsManager,
)

from django.utils.translation import gettext_lazy as _

from django.core.validators import EmailValidator


class CustomEmailValidator(EmailValidator):
    message = _("Please enter a valid email address.")


class UserCredentials(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"

    objects = UserCredentialsManager()

    email = models.CharField(
        max_length=255,
        unique=True,
        validators=[CustomEmailValidator()],
        error_messages={"unique": "This email address is already registered"},
    )

    is_staff = models.BooleanField(
        default=False,
    )

    groups = models.ManyToManyField(
        to="auth.Group",
        related_name="user_credential_details",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each group.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        to="auth.Permission",
        related_name="user_credential_details",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
