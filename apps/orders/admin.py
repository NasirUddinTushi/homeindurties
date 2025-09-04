from django.contrib import admin
from .models import Order, OrderItem, Discount


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total', 'created_at')
    search_fields = ('customer__email',)
    list_filter = ('created_at',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'unit_price')
    search_fields = ('order__id', 'product__name')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'is_active')
    search_fields = ('code',)
    list_filter = ('is_active', 'discount_type')
