from django.urls import path
from .views import ProductListView, CategoryListView, AttributeListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('attributes/', AttributeListView.as_view(), name='attribute-list'),
]
