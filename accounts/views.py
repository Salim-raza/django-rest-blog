from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .utils import get_tokens_for_user
from rest_framework import status
from drf_yasg import openapi


@swagger_auto_schema(
    method="post",
    operation_summary="User Registration",
    request_body=UserSerializer,
    responses={
        201: "Registration successful",
        400: "Validation error"
    }
)
# Registration API
@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response(
            {
                "message": "Registration successful",
                "user": UserSerializer(user).data
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )



@swagger_auto_schema(
    method="post",
    operation_summary="User Login",
    operation_description="Login using username and password.",
    request_body=LoginSerializer,
    responses={
        200: openapi.Response("Login successful"),
        400: "Missing username or password",
        401: "Invalid credentials"
    }
)
# Login API
@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = serializer.validated_data["email"]
    password = serializer.validated_data["password"]
    
    user = authenticate(
        request,
        username=email,
        password=password
    )
    if user is None:
        return Response({"error": "Invalid username or password"},status=status.HTTP_401_UNAUTHORIZED)
    
    return Response({
        "message": "Login successful",
        "user": UserSerializer(user).data,
        "tokens": get_tokens_for_user(user)
    }, status=status.HTTP_200_OK)