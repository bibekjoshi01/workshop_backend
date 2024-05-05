from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from src.core.models import Country
from src.base.models import AbstractInfoModel


class UserAddress(AbstractInfoModel):
    """User Address Model"""

    uuid = models.UUIDField(editable=False, default=uuid4, unique=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, verbose_name=_("Country/Region")
    )
    city = models.CharField(_("City"), max_length=100, blank=True)
    address = models.CharField(_("Address"), max_length=255, blank=True)

    class Meta:
        verbose_name = _("User Address")
        verbose_name_plural = _("User Addresses")

    def __str__(self):
        return f"{self.address}, {self.city}, {self.country}"
