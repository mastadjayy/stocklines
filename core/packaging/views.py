from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Packaging
from .forms import PackagingForm


class PackagingListView(ListView):
    """List All Packagings."""
    model = Packaging
    context_object_name = 'packagings'
    template_name = 'packaging/packagings.html'


class PackagingCreateView(View):
    """Create A Packaging."""
    form_class = PackagingForm
    template_name = 'packaging/create.html'

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
            return redirect('packaging:packagings')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class PackagingDetailView(DetailView):
#    model = Packaging
    template_name = 'packaging/detail.html'
    context_object_name = 'packaging'

    def get_object(self):
        model = get_object_or_404(Packaging, pk=self.kwargs['public_id'])
        return model
