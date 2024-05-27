from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Carrier
from .forms import CarrierForm


class CarrierListView(ListView):
    """List All Carriers."""
    model = Carrier
    context_object_name = 'carriers'
    template_name = 'carrier/carriers.html'


class CarrierCreateView(View):
    """Create A Carrier."""
    form_class = CarrierForm
    template_name = 'carrier/create.html'

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
            return redirect('carrier:carriers')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class CarrierDetailView(DetailView):
#    model = Carrier
    template_name = 'carrier/detail.html'
    context_object_name = 'carrier'

    def get_object(self):
        model = get_object_or_404(Carrier, pk=self.kwargs['public_id'])
        return model
