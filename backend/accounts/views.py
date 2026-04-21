# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.contrib.auth import authenticate
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import permission_classes
# from rest_framework_simplejwt.tokens import RefreshToken
# # from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model

# User = get_user_model()


# @api_view(["POST"])
# def register(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     email = request.data.get("email")

#     if User.objects.filter(username=username).exists():
#         return Response({"error": "User exists"}, status=400)

#     user = User.objects.create_user(username=username, password=password, email=email)

#     return Response({"message": "User created"})

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import sync_to_async
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re


@api_view(["POST"])
async def register(request):
    try:
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        # 1. Required fields validation
        if not username or not email or not password:
            return Response(
                {"status": "error", "message": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 2. Email validation
        try:
            validate_email(email)
        except ValidationError:
            return Response(
                {"status": "error", "message": "Invalid email format"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 3. Password validation (basic)
        if len(password) < 6:
            return Response(
                {
                    "status": "error",
                    "message": "Password must be at least 6 characters",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not re.search(r"[A-Z]", password):
            return Response(
                {
                    "status": "error",
                    "message": "Password must contain at least one uppercase letter",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not re.search(r"[0-9]", password):
            return Response(
                {
                    "status": "error",
                    "message": "Password must contain at least one number",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 4. Check if user exists
        exists = await sync_to_async(User.objects.filter(username=username).exists)()
        if exists:
            return Response(
                {"status": "error", "message": "Username already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 5. Create user (hashed + salted)
        user = await sync_to_async(User.objects.create_user)(
            username=username, email=email, password=password
        )

        # 6. Generate JWT
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status": "success",
                "message": "User registered successfully",
                "data": {
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                    "username": user.username,
                },
            },
            status=status.HTTP_201_CREATED,
        )

    except Exception as e:
        # Global error handling
        return Response(
            {
                "status": "error",
                "message": "Something went wrong",
                "error": str(e),  # remove in production
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# REGISTER
# @api_view(["POST"])
# def register(request):
#     user = User.objects.create_user(
#         username=request.data["username"], password=request.data["password"]
#     )
#     return Response({"message": "User created"})


# LOGIN
@api_view(["POST"])
def login_view(request):
    user = authenticate(
        username=request.data.get("username"), password=request.data.get("password")
    )

    if user:
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access": str(refresh.access_token),
            }
        )
    return Response({"error": "Invalid credentials"}, status=400)


# DASHBOARD (PROTECTED)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(request):
    return Response(
        {
            "message": f"Welcome {request.user.username}!",
            "data": "This is protected dashboard data",
        }
    )
