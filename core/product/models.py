from django.db import models
from django.urls import reverse

from core.abstract.models import (
    AbstractManager,
    AbstractModel
)


class ProductManager(AbstractManager):
    pass


class Product(AbstractModel):
    product_name = models.CharField(max_length=50, unique=True)

    objects = ProductManager()

    def __str__(self):
        return f"{self.product_name}"

#    def get_absolute_url(self):
#        return reverse("carrier:carrier_detail", kwargs={"id": self.public_id})