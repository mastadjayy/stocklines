from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product
from .forms import ProductForm


class ProductListView(ListView):
    """List All Products."""
    model = Product
    context_object_name = 'products'
    template_name = 'product/products.html'
    # Later on use prefetch_related() to display related Products on the view.


class ProductCreateView(View):
    """Create A Product."""
    form_class = ProductForm
    template_name = 'product/product_form.html'

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
            return redirect('product:products')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class ProductDetailView(DetailView):
#    model = Packaging
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        model = get_object_or_404(Product, pk=self.kwargs['public_id'])
        return model


def edit_product(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=Product)
        if form.is_valid():
            product = form.save()

            return redirect('product:products')
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'product/product_form.html',
        {'form': form}
    )