from django.db import models
from django.urls import reverse

from core.abstract.models import (
    AbstractManager,
    AbstractModel
)


class WarehouseManager(AbstractManager):
    pass

class Warehouse(AbstractModel):
    warehouse_name = models.CharField(max_length=50, unique=True)
    warehouse_type = models.ForeignKey(to="WarehouseType", blank=True, null=True, on_delete=models.SET_NULL)
    surface_area = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    volume = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fill_rate = models.CharField(max_length=20, default="", blank=True)
    capacity = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    objects = WarehouseManager()

    def __str__(self):
        return f"{self.warehouse_name}"
    
#    def get_absolute_url(self):
#        return reverse("warehouse:warehouse_edit", kwargs={"pk": self.pk})


class WarehouseTypeManager(AbstractManager):
    pass

class WarehouseType(AbstractModel):
    type_name = models.CharField(max_length=50, unique=True)

    objects = WarehouseTypeManager()

    def __str__(self):
        return f"{self.type_name}"