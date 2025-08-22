from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .models import Customer, CustomerAddress
from rest_framework import status

from .serializers import (
    CustomerRegisterSerializer,
    CustomerLoginSerializer,
    CustomerProfileSerializer,
    CustomerAddressSerializer
)

# Register
class RegisterView(APIView):
    permission_classes = []  # no auth needed

    def post(self, request):
        serializer = CustomerRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login
class LoginView(APIView):
    permission_classes = []  # No permission required for login

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authentication process
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)  # Session-based login
            return Response({"message": "Login successful", "user": email}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

# Logout
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"detail": "Logout successful"})

# Profile
class ProfileView(APIView):
    permission_classes = []

    def get(self, request):
        serializer = CustomerProfileSerializer(request.user)
        return Response(serializer.data)

# Customer Address
class CustomerAddressView(APIView):
    permission_classes = []

    def get(self, request):
        addresses = CustomerAddress.objects.filter(customer=request.user)
        serializer = CustomerAddressSerializer(addresses, many=True)
        return Response({
            "items": serializer.data,
            "count": addresses.count(),
            "hasMore": False,
            "limit": 25,
            "offset": 0
        })
