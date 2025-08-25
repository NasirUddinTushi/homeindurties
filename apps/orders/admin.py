from django.contrib import admin
from .models import Order, OrderItem, Discount 
from unfold.admin import ModelAdmin

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('id', 'customer', 'total', 'created_at')
    search_fields = ('customer__email',)

@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'unit_price')

@admin.register(Discount)
class DiscountAdmin(ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'is_active')
