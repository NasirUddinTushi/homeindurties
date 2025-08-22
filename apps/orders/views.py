from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem, Discount
from .serializers import OrderSerializer, DiscountSerializer
from apps.accounts.models import Customer, CustomerAddress
from rest_framework.permissions import AllowAny

class OrderCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        customer_payload = data["customer_payload"]
        shipping_info = customer_payload["shipping_info"]

        # Login user
        if customer_payload.get("customer_id"):
            try:
                customer = Customer.objects.get(id=customer_payload["customer_id"])
            except Customer.DoesNotExist:
                return Response({"error": "Customer not found."}, status=status.HTTP_400_BAD_REQUEST)

        # Guest user
        else:
            customer = Customer.objects.filter(email=shipping_info["email"]).first()
            if not customer:
                customer = Customer.objects.create(
                    email=shipping_info["email"],
                    first_name=shipping_info["firstName"],
                    last_name=shipping_info["lastName"],
                )
                if shipping_info.get("password"):
                    customer.set_password(shipping_info["password"])
                    customer.save()

        # Create shipping address
        shipping_address = CustomerAddress.objects.create(
            customer=customer,
            street_address=shipping_info["address"],
            city=shipping_info["city"],
            country=shipping_info["country"],
            postal_code=shipping_info["postalCode"],
            address_type="shipping",
            is_default=True
        )

        # Create order
        order = Order.objects.create(
            customer=customer,
            shipping_address=shipping_address,
            payment_method=data["payment_method"],
            subtotal=data["summary"]["subtotal"],
            delivery_charge=data["summary"]["delivery"],
            discount_code=data["summary"].get("discount_code"),
            discount_amount=data["summary"]["discount_amount"],
            total=data["summary"]["total"],
        )

        # Create order items
        for item in data["order_items"]:
            order_item = OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["quantity"],
                unit_price=item["unit_price"],
            )
            if "attributes" in item:
                order_item.attributes.set(item["attributes"])

        return Response(
            {"success": True, "message": "Order placed successfully!", "order_id": order.id},
            status=status.HTTP_201_CREATED
        )


class DiscountListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, code):
        try:
            discount = Discount.objects.get(code=code, is_active=True)
            serializer = DiscountSerializer(discount)
            return Response({
                "MapList": [serializer.data],
                "Message": "Data Loaded.",
                "Code": "200",
                "Status": "Success"
            })

        except Discount.DoesNotExist:
            return Response({
                "Message": "Discount code not found.",
                "Code": "404",
                "Status": "Error"
            }, status=status.HTTP_404_NOT_FOUND)
