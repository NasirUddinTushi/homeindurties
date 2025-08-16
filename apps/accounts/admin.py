from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, CustomerAddress

@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    model = Customer
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']

@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'street_address', 'city', 'postal_code', 'is_default']
