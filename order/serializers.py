from rest_framework import serializers

from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_amount(self, obj):
        amount = obj.product.price * obj.quantity
        return amount


class OrderSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_amount(self, obj):
        total_amount = sum(item.product.price * item.quantity for item in obj.order_items.all())
        return total_amount
