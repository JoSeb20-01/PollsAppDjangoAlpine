from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class BaseSoftDeleteModel(models.Model):

    STATE_FIELD: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._check_state_field()

    def _check_state_field(self):
        if not self.STATE_FIELD:
            raise Exception("STATE_FIELD hadn't been declared.")

    def soft_delete(self):
        setattr(self, self.STATE_FIELD, False)
        self.save()

    def restore(self):
        setattr(self, self.STATE_FIELD, True)
        self.save()

    class Meta:
        abstract = True


class SoftDeleteModel(BaseSoftDeleteModel):
    STATE_FIELD = "is_active"
    is_active = models.BooleanField(_("state"), default=True, blank=True)

    class Meta:
        abstract = True


class SoftDeleteModelWithDateTime(BaseSoftDeleteModel):
    delete_date = models.DateTimeField(_("delete_date"), default=None)

    def soft_delete(self):
        self.delete_date = timezone.now()
        super().soft_delete()

    def restore(self):
        self.delete_date = None
        super().restore()

    class Meta:
        abstract = True
