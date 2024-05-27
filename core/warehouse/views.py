from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Warehouse
from .forms import (
    WarehouseForm,
)


class WarehouseListView(ListView):
    """List All Warehouses."""
    model = Warehouse
    context_object_name = 'warehouses'
    template_name = 'warehouse/warehouses.html'
    # Later on use prefetch_related() to display related warehouses on the view.


class WarehouseCreateView(View):
    """Create A Warehouse."""
    form_class = WarehouseForm
    template_name = 'warehouse/warehouse_form.html'

    def get(self, request):
        form = self.form_class(request.GET or None)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouse:warehouses')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class WarehouseDetailView(DetailView):
#    model = Warehouse
    template_name = 'warehouse/detail.html'
    context_object_name = 'warehouse'

    def get_object(self):
        model = get_object_or_404(Warehouse, pk=self.kwargs['public_id'])
        return model


def edit_warehouse(request, pk):
    warehouse = get_object_or_404(Warehouse, id=pk)

    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            warehouse = form.save()

            # Now let's handle associated products
#            product_ids = request.POST.getlist('products', [])
#            products = Product.objects.filter(pk__in=product_ids)
#            client.products.set(products)

            return redirect('warehouse:warehouses')
    else:
        form = WarehouseForm(instance=warehouse)

    return render(
        request,
        'warehouse/warehouse_form.html',
        {'form': form}
    )