"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
