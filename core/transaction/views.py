from django.shortcuts import render, redirect
from django.views import View

from .models import (
    StockIn,
    StockOut
)

from .forms import (
    StockInForm,
    StockOutForm
)


def stock_in_list_view(request):

    stock_in_list = StockIn.objects.all()

    context = {
        'stock_in_list': stock_in_list
    }
    
    return render(request, 'transaction/stock_in/list.html', context)


class StockInView(View):
    template_name = 'transaction/stock_in/create.html'

    def get(self, request):
        form = StockInForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StockInForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('transaction:stock_in_list')  # Redirect to a success page

        return render(request, self.template_name, {'form': form})


def stock_out_list_view(request):

    stock_out_list = StockOut.objects.all()

    context = {
        'stock_out_list': stock_out_list
    }

    return render(request, 'transaction/stock_out/list.html', context)



class StockOutView(View):
    template_name = 'transaction/stock_out/create.html'

    def get(self, request):
        form = StockOutForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = StockOutForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('transaction:stock_out_list')  # Redirect to a success page

        return render(request, self.template_name, {'form': form})
    


"""    


    def post(self, request):
        form = StockTransactionForm(request.POST, transaction_type='OUT')
        if form.is_valid():
            product = form.cleaned_data['product']
            warehouse = form.cleaned_data['warehouse']
            client = form.cleaned_data['client']
            quantity = form.cleaned_data['quantity']

            # Check if there is enough stock to fulfill the request
            available_stock = Stock.objects.filter(
                product=product,
                warehouse=warehouse,
                client=client
            ).aggregate(models.Sum('quantity'))['quantity__sum'] or 0

            if available_stock >= quantity:
                Stock.objects.create(
                    product=product,
                    warehouse=warehouse,
                    client=client,
                    quantity=-quantity,
                    transaction_type='OUT'
                )
                return redirect('stock_out_success')  # Redirect to a success page
            else:
                # Handle insufficient stock case
                messages.error(request, 'Insufficient stock to fulfill the request.')

        return render(request, self.template_name, {'form': form}) """
