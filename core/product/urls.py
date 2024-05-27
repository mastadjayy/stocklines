from django.urls import path

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
#    edit_product,
)

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('create/', ProductCreateView.as_view(), name='product_form'),
    path('<str:public_id>/', ProductDetailView.as_view(), name='product_detail'),
#    path('<str:public_id>/', edit_product, name='product_edit'),
]
