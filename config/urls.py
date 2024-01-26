from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from account.views import VendorViewSet
from product.views import CategoryViewSet
from .drf_swagger import urlpatterns as doc_urls


router = routers.DefaultRouter()
router.register(r'api/v1/vendor', VendorViewSet)
router.register(r'api/v1/category', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/account/', include('account.urls')),

    path('api/v1/product/', include('product.urls')),

]

urlpatterns += router.urls  # vendor

urlpatterns += doc_urls  # swagger docs urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
