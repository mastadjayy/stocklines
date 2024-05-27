from django.urls import path

from .views import (
    PackagingListView,
    PackagingCreateView,
    PackagingDetailView,
)

app_name = 'packaging'

urlpatterns = [
    path('', PackagingListView.as_view(), name='packagings'),
    path('create/', PackagingCreateView.as_view(), name='packaging_create'),
    path('<str:public_id>/', PackagingDetailView.as_view(), name='packaging_detail'),
]
