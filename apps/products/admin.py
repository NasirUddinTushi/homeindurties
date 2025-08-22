from django.contrib import admin
from .models import Product, Category, ProductImage, Attribute, AttributeValue
from unfold.admin import ModelAdmin

# Category Admin
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
    list_filter = ('parent',)

# Product Admin
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category', 'price', 'is_bestseller', 'is_new')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
    list_filter = ('category', 'is_bestseller', 'is_new')
    inlines = [ProductImageInline]

#  Register ProductImage for changelist
@admin.register(ProductImage)
class ProductImageAdmin(ModelAdmin):
    list_display = ('id', 'product', 'image')

# Attribute Admin
@admin.register(Attribute)
class AttributeAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(AttributeValue)
class AttributeValueAdmin(ModelAdmin):
    list_display = ('id', 'attribute', 'value')
    search_fields = ('value', 'attribute__name')
