# Use UUID as pk
import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.abstract.models import (
    AbstractModel,
    AbstractManager,
)


class CarrierManager(AbstractManager):
    pass


class Carrier(AbstractModel):
    carrier_name = models.CharField(_("Name of Carrier"), max_length=100, unique=True)

    objects = CarrierManager()

    def __str__(self):
        return f"{self.carrier_name}"
    
#    def get_absolute_url(self):
#        return reverse("carrier:carrier_detail", kwargs={"pk": self.id})