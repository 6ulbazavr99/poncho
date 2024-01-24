from django.urls import path
from rest_framework import routers

from product.views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
]


urlpatterns += router.urls
