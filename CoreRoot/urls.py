from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import (
    dashboard_view,
    administration_view,
    referentiel_view,
)

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('core.accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('warehouses/', include('core.warehouse.urls', namespace='warehouse')),
    path('products/', include('core.product.urls', namespace='product')),
    path('clients/', include('core.client.urls', namespace='client')),
    path('carriers/', include('core.carrier.urls', namespace='carrier')),
    path('packagings/', include('core.packaging.urls', namespace='packaging')),
    path('transactions/', include('core.transaction.urls', namespace='transaction')),

    path('administration/', administration_view, name='administration_landing'),
    path('administration/referentiel/', referentiel_view, name='referentiel'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)