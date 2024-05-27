from django.urls import path

from .views import (
    CarrierListView,
    CarrierCreateView,
    CarrierDetailView,
)

app_name = 'carrier'

urlpatterns = [
    path('', CarrierListView.as_view(), name='carriers'),
    path('create/', CarrierCreateView.as_view(), name='carrier_create'),
    path('<str:public_id>/', CarrierDetailView.as_view(), name='carrier_detail'),
]
