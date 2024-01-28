from rest_framework import routers

from .views import OrderViewSet, OrderItemViewSet

router = routers.DefaultRouter()
router.register(r'', OrderViewSet)
router.register(r'item', OrderItemViewSet)

urlpatterns = [
]


urlpatterns += router.urls
