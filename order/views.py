from django.shortcuts import render
from rest_framework import viewsets

from order.models import Order, OrderItem
from order.serializers import OrderSerializer, OrderItemSerializer, OrderListSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        return OrderSerializer

    # def perform_create(self, serializer):
    #     serializer.save()
