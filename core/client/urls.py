from django.urls import path

from .views import (
    ClientListView,
    create_client,
    ClientDetailView,
#    edit_client,
)

app_name = 'client'

urlpatterns = [
    path('', ClientListView.as_view(), name='clients'),
    path('create/', create_client, name='client_form'),
    path('<str:public_id>/', ClientDetailView.as_view(), name='client_detail'),
]
