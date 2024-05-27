from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from core.product.models import Product
from .models import Client
from .forms import ClientForm


class ClientListView(ListView):
    """List all clients."""
    model = Client
    context_object_name = 'clients'
    template_name = 'client/clients.html'


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()

            # Now, let's handle associated products
            product_ids = request.POST.getlist('products')
            products = Product.objects.filter(pk__in=product_ids)
            client.products.set(products)
            
            return redirect('client:clients')
    else:
        form = ClientForm()

    products = Product.objects.all()
    return render(request, 'client/client_form.html', {'form': form, 'products': products})


class ClientDetailView(DetailView):
    template_name = 'client/detail.html'
    context_object_name = 'client'

    def get_object(self):
        model = get_object_or_404(Client, pk=self.kwargs['public_id'])
        return model


def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()

            # Now let's handle associated products
            product_ids = request.POST.getlist('products', [])
            products = Product.objects.filter(pk__in=product_ids)
            client.products.set(products)

            return redirect('warehouse:clients')
    else:
        form = ClientForm(instance=client)

    products = Product.objects.all()
    return render(
        request,
        'warehouse/clients/edit_client.html',
        {'form': form, 'client': client, 'products': products}
    )
