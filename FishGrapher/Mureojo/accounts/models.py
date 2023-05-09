from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class AuthKey(models.Model):  # 인증번호 전용 model
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    auth = models.CharField(max_length=8, blank=True, null=True)
