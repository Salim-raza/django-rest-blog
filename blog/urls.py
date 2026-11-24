from django.urls import path
from .views import blog_list_create, blog_details

urlpatterns = [
    path("create_list/", blog_list_create, name="blog_list_create"),
    path("update_delete/<slug:slug>/", blog_details, name="blog_details"),
]