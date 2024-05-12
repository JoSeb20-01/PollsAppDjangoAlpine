from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core.soft_delete.models import BaseSoftDeleteModel


# Create your models here.
class User(AbstractUser, BaseSoftDeleteModel):
    STATE_FIELD = "is_active"
    image = models.ImageField(_("image"), upload_to="", null=True)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
