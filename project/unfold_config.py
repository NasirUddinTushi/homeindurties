from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "HomeTexIndustries Admin",
    "SITE_HEADER": "HomeTexIndustries",
    "SITE_URL": "/",
    "SITE_SYMBOL": "settings",

    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,  # শুধু custom apps দেখাতে চাইলে False
        "navigation": [
            # Dashboard
            {
                "title": "Dashboard",
                "items": [
                    {"title": "Home", "icon": "dashboard", "link": reverse_lazy("admin:index")},
                ],
            },

            # Products App
            {
                "title": "Products Management",
                "separator": True,
                "items": [
                    {
                        "title": "Categories",
                        "icon": "category",
                        "link": reverse_lazy("admin:products_category_changelist"),
                    },
                    {
                        "title": "Products",
                        "icon": "inventory_2",
                        "link": reverse_lazy("admin:products_product_changelist"),
                    },
                    {
                        "title": "Product Images",
                        "icon": "image",
                        "link": reverse_lazy("admin:products_productimage_changelist"),
                    },
                    {
                        "title": "Attributes",
                        "icon": "tune",
                        "link": reverse_lazy("admin:products_attribute_changelist"),
                    },
                    {
                        "title": "Attribute Values",
                        "icon": "label",
                        "link": reverse_lazy("admin:products_attributevalue_changelist"),
                    },
                ],
            },

            # Orders App
            {
                "title": "Orders Management",
                "separator": True,
                "items": [
                    {
                        "title": "Orders",
                        "icon": "shopping_cart",
                        "link": reverse_lazy("admin:orders_order_changelist"),
                    },
                    {
                        "title": "Order Items",
                        "icon": "receipt",
                        "link": reverse_lazy("admin:orders_orderitem_changelist"),
                    },
                    {
                        "title": "Discounts",
                        "icon": "card_giftcard",
                        "link": reverse_lazy("admin:orders_discount_changelist"),
                    },
                ],
            },

            # Accounts App
            {
                "title": "Customer Management",
                "separator": True,
                "items": [
                    {
                        "title": "Customers",
                        "icon": "person",
                        "link": reverse_lazy("admin:accounts_customer_changelist"),
                    },
                    {
                        "title": "Addresses",
                        "icon": "location_on",
                        "link": reverse_lazy("admin:accounts_customeraddress_changelist"),
                    },
                ],
            },

        ],
    },
}
