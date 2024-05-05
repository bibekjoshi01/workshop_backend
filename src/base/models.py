from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AbstractInfoModel(models.Model):
    """Abstract Created Info Model"""

    created_at = models.DateTimeField(
        _("created date"), default=timezone.now, editable=False
    )
    updated_at = models.DateTimeField(_("date updated"), auto_now=True)
    created_by = models.ForeignKey("user.User", on_delete=models.PROTECT)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this object should be treated as active. "
            "Unselect this instead of deleting instances."
        ),
    )

    class Meta:
        abstract = True
