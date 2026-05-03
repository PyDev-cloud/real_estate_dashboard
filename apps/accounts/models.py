
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('investor', 'Investor'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    email=models.EmailField(unique=True)
    def is_admin(self):
        return self.user_type == 'admin'

    def is_investor(self):
        return self.user_type == 'investor'