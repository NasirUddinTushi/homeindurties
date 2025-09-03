from django.contrib import admin
from unfold.admin import ModelAdmin

# ---------------------
# Products models
# ---------------------
from .models import (
    Product, ProductImage, Category, Attribute, AttributeValue, ProductAttribute
)

# ---------------------
# Products Admin
# ---------------------

# Category Admin
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
    list_filter = ('parent',)


# ProductImage Inline
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


# ProductAttribute Inline
class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


# Product Admin
@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category', 'price', 'is_bestseller', 'is_new')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
    list_filter = ('category', 'is_bestseller', 'is_new')
    inlines = [ProductImageInline, ProductAttributeInline]


# Attribute Admin
@admin.register(Attribute)
class AttributeAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(AttributeValue)
class AttributeValueAdmin(ModelAdmin):
    list_display = ('id', 'attribute', 'value')
    search_fields = ('value', 'attribute__name')


# -------------------------------------------------
# Orders Admin
# -------------------------------------------------
# import orders admin separately
from apps.orders.models import Order, OrderItem, Discount

# Only register here if not already registered
if not admin.site.is_registered(Order):
    @admin.register(Order)
    class OrderAdmin(ModelAdmin):
        list_display = ('id', 'customer', 'total', 'created_at')
        search_fields = ('customer__email',)


if not admin.site.is_registered(OrderItem):
    @admin.register(OrderItem)
    class OrderItemAdmin(ModelAdmin):
        list_display = ('id', 'order', 'product', 'quantity', 'unit_price')
        inlines = []  # ManyToMany handled via ProductAttribute


if not admin.site.is_registered(Discount):
    @admin.register(Discount)
    class DiscountAdmin(ModelAdmin):
        list_display = ('code', 'discount_type', 'discount_value', 'is_active')
