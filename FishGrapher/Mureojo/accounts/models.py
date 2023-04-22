from djongo import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    is_authenticated = True
    is_anonymous = False

    def __str__(self):
        return self.username
