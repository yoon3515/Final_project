from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.

class AuthKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auth = models.CharField(max_length=8, blank=True, null=True)
