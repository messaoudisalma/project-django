from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('payment.urls', namespace='payment')),
    path('account/', include('account.urls', namespace='account')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('', include('store.urls', namespace='store')),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
