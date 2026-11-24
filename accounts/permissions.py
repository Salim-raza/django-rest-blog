from rest_framework.permissions import BasePermission
from .models import CustomUser


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.role == "author"
    
    
class IsViewer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.role == "viewer"
    
    
class IsAuthorORIsViewer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False 
        return user.role in ("author", "viewer")