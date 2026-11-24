from django.contrib.auth.models import AbstractUser
from .usermanager import CustomUserManager
from django.db import models


class CustomUser(AbstractUser):
    
    class RoleChoice(models.TextChoices):
        AUTHOR = "author", "Author"
        VIEWER = "viewer", "Viewer"

    username = None
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=RoleChoice.choices,
        default=RoleChoice.VIEWER
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email