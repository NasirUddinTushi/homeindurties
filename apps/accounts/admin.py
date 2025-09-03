from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, CustomerAddress
from unfold.admin import ModelAdmin


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    model = Customer
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']

    # date_joined & last_login read-only হবে
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )


@admin.register(CustomerAddress)
class CustomerAddressAdmin(ModelAdmin):
    list_display = ['customer', 'street_address', 'city', 'postal_code', 'is_default', 'created_at']
    search_fields = ['customer__email', 'street_address', 'city']
