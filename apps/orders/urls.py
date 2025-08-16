from django.urls import path
from .views import OrderCreateAPIView, DiscountListAPIView

urlpatterns = [
    path('create-order/', OrderCreateAPIView.as_view(), name='create-order'),
    # path('discounts/', DiscountListAPIView.as_view(), name='discount-list'),
    path('discounts/<str:code>/', DiscountListAPIView.as_view(), name='discount-list'),

]
