
from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "slug", "description", "author", "created_at", "update_at"]
        read_only_fields = ["id", "slug", "author", "created_at", "update_at",]
