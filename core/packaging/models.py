from django.db import models

from core.abstract.models import (
    AbstractManager,
    AbstractModel,
)


class PackagingManager(AbstractManager):
    pass


class Packaging(AbstractModel):
    pack_type = models.CharField(max_length=50, unique=True)

    objects = PackagingManager()

    def __str__(self):
        return f"{self.pack_type}"
