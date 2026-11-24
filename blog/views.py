from rest_framework.decorators import api_view, permission_classes, authentication_classes
from accounts.permissions import IsAuthor, IsAuthorORIsViewer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import BlogSerializer
from rest_framework import status
from drf_yasg import openapi
from .models import Blog

# Create your views here.
@swagger_auto_schema(
    methods=["GET"],
    operation_summary="Get All Blogs",
    operation_description="Retrieve all blog posts.",
    responses={
        200: BlogSerializer(many=True),
        401: "Authentication required."
    }
)
@swagger_auto_schema(
    methods=["POST"],
    operation_summary="Create Blog",
    operation_description="Only Author can create a blog post.",
    request_body=BlogSerializer,
    responses={
        201: BlogSerializer,
        400: "Validation Error",
        401: "Authentication required.",
        403: "Only Author can create blog."
    }
)
@api_view(["GET", "POST"])
@permission_classes([IsAuthorORIsViewer])
@authentication_classes([JWTAuthentication])
def blog_list_create(request):
    
    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    if not IsAuthor().has_permission(request, None):
        return Response(
            {"detail": "Only Author can create blog."},
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


slug_parameter = openapi.Parameter(
    "slug",
    openapi.IN_PATH,
    description="Enter the blog slug",
    type=openapi.TYPE_STRING,
    required=True
)


@swagger_auto_schema(
    methods=["GET"],
    operation_summary="Get Blog Details",
    operation_description="Retrieve blog details using slug.",
    manual_parameters=[slug_parameter],
    responses={
        200: BlogSerializer,
        404: "Blog not found."
    }
)
@swagger_auto_schema(
    methods=["PUT", "PATCH"],
    operation_summary="Update Blog",
    operation_description="Update blog using slug. Only the owner Author can update.",
    manual_parameters=[slug_parameter],
    request_body=BlogSerializer,
    responses={
        200: BlogSerializer,
        400: "Validation Error",
        403: "Permission denied.",
        404: "Blog not found."
    }
)
@swagger_auto_schema(
    methods=["DELETE"],
    operation_summary="Delete Blog",
    operation_description="Delete blog using slug. Only the owner Author can delete.",
    manual_parameters=[slug_parameter],
    responses={
        200: "Blog deleted successfully.",
        403: "Permission denied.",
        404: "Blog not found."
    }
)
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthorORIsViewer])
@authentication_classes([JWTAuthentication])
def blog_details(request, slug):

    blog = get_object_or_404(Blog, slug=slug)

    if request.method == "GET":
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    if not IsAuthor().has_permission(request, None):
        return Response(
            {"detail": "Only Author can update or delete blog."},
            status=status.HTTP_403_FORBIDDEN
        )
        
    if blog.author != request.user:
        return Response(
            {"detail": "You can only modify your own blog."},
            status=status.HTTP_403_FORBIDDEN
        )

    if request.method in ["PUT", "PATCH"]:
        serializer = BlogSerializer(
            blog,
            data=request.data,
            partial=request.method == "PATCH"
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == "DELETE":
        blog.delete()
        return Response(
            {"detail": "Blog deleted successfully."},
            status=status.HTTP_200_OK
        )
