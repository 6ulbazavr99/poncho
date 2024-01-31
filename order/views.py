from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        items = self.request.data.get('items', [])
        for item in items:
            quantity = item.get('quantity', 1)
            OrderItem.objects.create(
                order=order,
                product_id=item['product'],
                quantity=quantity
            )
