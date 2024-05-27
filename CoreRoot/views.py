import calendar
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import (
    ExtractMonth,
    ExtractYear,
)

from core.transaction.models import (
    StockIn,
    StockOut,
)


@login_required
def dashboard_view(request):
    # Stock In Per Month
    stock_in_per_month = StockIn.objects.annotate(
        month=ExtractMonth('date_entry')
    ).order_by('month').values('month').annotate(total=Count('public_id'))
    stock_in_months = [] # Months
    stock_in_count = [] # Count of Stock IN
    for stock_in_data in stock_in_per_month:
            stock_in_months.append(calendar.month_name[stock_in_data['month']])
            stock_in_count.append(stock_in_data['total'])

    # Stock Out Per Month
    stock_out_per_month = StockOut.objects.annotate(
         month=ExtractMonth('date_exit')
    ).order_by('month').values('month').annotate(total=Count('public_id'))
    stock_out_months = [] # Months
    stock_out_count = [] # Count of Stock OUT
    for stock_out_data in stock_out_per_month:
            stock_out_months.append(calendar.month_name[stock_out_data['month']])
            stock_out_count.append(stock_out_data['total'])

    context = {
        'stock_in_months': stock_in_months,
        'stock_in_count': stock_in_count,
        'stock_out_months': stock_out_months,
        'stock_out_count': stock_out_count,
    }

    return render(request, 'pages/dashboard.html', context)


def administration_view(request):
    context = {}
    return render(
        request,
        'pages/administration/administration_landing.html',
        context
    )


def referentiel_view(request):
    context = {}
    return render(
        request,
        'pages/administration/referentiel.html',
        context
    )