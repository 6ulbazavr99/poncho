from django.contrib import admin
from order.models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total_amount', )


class OrderItemAdmin(admin.ModelAdmin):
    readonly_fields = ('amount', )
#
#
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

# admin.site.register(Order)
# admin.site.register(OrderItem)