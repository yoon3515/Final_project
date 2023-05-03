from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    auth = models.CharField(max_length=8, blank=True, null=True)
