from django.urls import path

from .views import (
    WarehouseListView,
    WarehouseCreateView,
    WarehouseDetailView,
#    edit_warehouse,
)

app_name = 'warehouse'

urlpatterns = [
    path('', WarehouseListView.as_view(), name='warehouses'),
    path('create/', WarehouseCreateView.as_view(), name='warehouse_form'),
    path('<str:public_id>/', WarehouseDetailView.as_view(), name='warehouse_detail'),
]
