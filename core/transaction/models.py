from django.db import models
from django.utils.translation import gettext_lazy as _

from core.abstract.models import (
    AbstractManager,
    AbstractModel
)

from core.carrier.models import Carrier
from core.client.models import Client
from core.packaging.models import Packaging
from core.product.models import Product
from core.warehouse.models import Warehouse


class BaseStockManager(AbstractManager):
    pass


class BaseStock(AbstractModel):
    """Base model for StockIn & StockOut models."""
    class Flux(models.TextChoices):
        IMPORT = "IMP", _("Import")
        EXPORT = "EXP", _("Export")

    flux = models.CharField(
        max_length=5,
        choices=Flux.choices,
        default='',
    )

    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    warehouse = models.ForeignKey(to=Warehouse, on_delete=models.CASCADE)
    carrier = models.ForeignKey(to=Carrier, on_delete=models.CASCADE, null=True)
    packaging = models.ForeignKey(to=Packaging, on_delete=models.CASCADE, null=True)
    display_id = models.IntegerField(default=1)
    shipment_num = models.CharField(max_length=50, blank=True, default='')

    objects = BaseStockManager()

    class Meta:
        abstract = True


class StockIn(BaseStock):
    class TypeGestion(models.TextChoices):
        LOT = "LT", _("Lot")
        MASSE = "MA", _("Masse")
        VRAC = "VR", _("Vrac")

    type_gestion = models.CharField(
        max_length=5,
        choices=TypeGestion.choices,
        default=TypeGestion.LOT,
    )

    nbr_lot = models.PositiveIntegerField(blank=True, null=True)
    campagne = models.CharField(max_length=5, default='', blank=True)
    num_contrat = models.CharField(max_length=5, default='', blank=True)
    date_entry = models.DateField()
    comment = models.TextField(blank=True, null=True)
    # Transporteur info
    num_immatricule = models.CharField(max_length=50, blank=True, default='')
    num_bordereau = models.CharField(max_length=50, blank=True, default='')
    num_remorque = models.CharField(max_length=50, blank=True, default='')
    nom_superviseur = models.CharField(max_length=50, blank=True, default='')
    nom_gardien = models.CharField(max_length=50, blank=True, default='')
    nom_chauffeur = models.CharField(max_length=50, blank=True, default='')
    permis_conduire = models.CharField(max_length=50, blank=True, default='')
    # Contenant info
    num_lot = models.CharField(max_length=50, blank=True, default='')
    quality = models.CharField(max_length=50, blank=True, default='')
    grade = models.CharField(max_length=50, blank=True, default='')
    conformity = models.CharField(max_length=50, blank=True, default='')
    poids_theorique = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    poids_reel  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    transaction_type = models.CharField(max_length=3, default='IN')

    class Meta:
        unique_together = ("product", "warehouse", "client", "created")
        ordering = ('-created',)
    
    def save(self, *args, **kwargs):
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = self.objects.all().aggregate(largest=models.Max('display_id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.display_id = last_id + 1

        super(StockIn, self).save(*args, **kwargs)


class StockOut(BaseStock):
    class TypeGestion(models.TextChoices):
        LOT = "LT", _("Lot")
        MASSE = "MA", _("Masse")
        VRAC = "VR", _("Vrac")

    type_gestion = models.CharField(
        max_length=5,
        choices=TypeGestion.choices,
        default=TypeGestion.LOT,
    )

    nbr_lot = models.PositiveIntegerField(blank=True, null=True)
    campagne = models.CharField(max_length=5, default='', blank=True)
    num_contrat = models.CharField(max_length=5, default='', blank=True)
    date_exit = models.DateField()
    comment = models.TextField(blank=True, null=True)
    # Transporteur info
    num_immatricule = models.CharField(max_length=50, blank=True, default='')
    num_bordereau = models.CharField(max_length=50, blank=True, default='')
    num_remorque = models.CharField(max_length=50, blank=True, default='')
    nom_superviseur = models.CharField(max_length=50, blank=True, default='')
    nom_gardien = models.CharField(max_length=50, blank=True, default='')
    nom_chauffeur = models.CharField(max_length=50, blank=True, default='')
    permis_conduire = models.CharField(max_length=50, blank=True, default='')
    # Contenant info
    num_lot = models.CharField(max_length=50, blank=True, default='')
    quality = models.CharField(max_length=50, blank=True, default='')
    grade = models.CharField(max_length=50, blank=True, default='')
    conformity = models.CharField(max_length=50, blank=True, default='')
    poids_theorique = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    poids_reel  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    transaction_type = models.CharField(max_length=3, default='OUT')

    class Meta:
        unique_together = ("product", "warehouse", "client", "created")
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_id = self.objects.all().aggregate(largest=models.Max('display_id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_id is not None:
                self.display_id = last_id + 1

        super(StockOut, self).save(*args, **kwargs)