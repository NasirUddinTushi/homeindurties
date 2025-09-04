from django.urls import path
from .views import OrderCreateAPIView, DiscountListAPIView

app_name = "orders"

urlpatterns = [
    path("create-order/",       OrderCreateAPIView.as_view(),  name="create-order"),
    # যদি কোড ছাড়া সব ডিসকাউন্ট লাগতো: path("discounts/", DiscountListAPIView.as_view(), name="discount-list"),
    path("discounts/<str:code>/", DiscountListAPIView.as_view(), name="discount-list"),
]
