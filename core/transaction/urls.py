from django.urls import path
from .views import (
    stock_in_list_view,
    StockInView,
    stock_out_list_view,
    StockOutView,
)

app_name = 'transaction'

urlpatterns = [
    # Your existing URL patterns
    path('entree-magasin/liste/', stock_in_list_view, name='stock_in_list'),
    path('entree-magasin/', StockInView.as_view(), name='stock_in'),
    
    path('sortie-magasin/liste/', stock_out_list_view, name='stock_out_list'),
    path('sortie-magasin/', StockOutView.as_view(), name='stock_out'),
#    path('stock-in/success/', success_view, name='stock_in_success'),
#    path('stock-out/success/', success_view, name='stock_out_success'),
]
