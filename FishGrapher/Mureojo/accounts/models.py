from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    # 추가 필드는 여기에 작성

    def __str__(self):
        return self.email