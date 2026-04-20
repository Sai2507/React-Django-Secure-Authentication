from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(["POST"])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if User.objects.filter(username=username).exists():
        return Response({"error": "User exists"}, status=400)

    user = User.objects.create_user(username=username, password=password, email=email)

    return Response({"message": "User created"})


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
