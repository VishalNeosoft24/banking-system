from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class User(AbstractUser):
    mobile_number = models.CharField(max_length=15, unique=True, help_text="Enter a valid mobile number")
    address = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.mobile_number})"