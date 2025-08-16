from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem, Discount
from .serializers import OrderSerializer, DiscountSerializer
from apps.accounts.models import Customer, CustomerAddress

class OrderCreateAPIView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            customer_data = data['customer_payload']
            shipping_info = customer_data['shipping_info']

            # Guest user: create Customer
            if not customer_data.get('customer_id'):
                customer = Customer.objects.create(
                    first_name=shipping_info['firstName'],
                    last_name=shipping_info['lastName'],
                    email=shipping_info['email']
                )
            else:
                customer = Customer.objects.get(id=customer_data['customer_id'])

            # Create shipping address
            address = CustomerAddress.objects.create(
                customer=customer,
                street_address=shipping_info['address'],
                city=shipping_info['city'],
                state="",
                country=shipping_info['country'],
                postal_code=shipping_info['postalCode'],
                address_type="shipping",
                is_default=True
            )

            summary = data['summary']

            order = Order.objects.create(
                customer=customer,
                shipping_address=address,
                payment_method=data['payment_method'],
                subtotal=summary['subtotal'],
                delivery_charge=summary['delivery'],
                discount_code=summary.get('discount_code'),
                discount_amount=summary['discount_amount'],
                total=summary['total']
            )

            # Order items
            for item in data['order_items']:
                order_item = OrderItem.objects.create(
                    order=order,
                    product_id=item['product']['id'],
                    quantity=item['quantity'],
                    unit_price=item['unit_price']
                )
                order_item.attributes.set(item['attributes'])
                order_item.save()

            return Response({"message": "Order created successfully", "order_id": order.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiscountListAPIView(APIView):
    def get(self, request, code):
        try:
            # Fetch the discount based on the provided code
            discount = Discount.objects.get(code=code, is_active=True)
            serializer = DiscountSerializer(discount)
            
            # Return the response in the desired format
            return Response({
                "MapList": [serializer.data],
                "Message": "Data Loaded.",
                "Code": "200",
                "Status": "Success"
            })

        except Discount.DoesNotExist:
            # Handle case where the discount code does not exist
            return Response({
                "Message": "Discount code not found.",
                "Code": "404",
                "Status": "Error"
            }, status=status.HTTP_404_NOT_FOUND)