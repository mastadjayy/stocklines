from django.db import models
from django.urls import reverse

from core.abstract.models import (
    AbstractManager,
    AbstractModel
)

from core.product.models import Product


class ClientManager(AbstractManager):
    pass


class Client(AbstractModel):
    client_name = models.CharField(max_length=50, unique=True)
    client_ref = models.CharField(max_length=100, blank=True, default='')
    client_address = models.CharField(max_length=100, default='', blank=True)
    client_email = models.CharField(max_length=30, default='', blank=True)
    client_phone = models.CharField(max_length=20, default='', blank=True)

    products = models.ManyToManyField(Product, blank=True)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ClientManager()

    def __str__(self):
        return f"{self.client_name}"
    
#    def get_absolute_url(self):
#        return reverse("client:client_edit", kwargs={"pk": self.pk})