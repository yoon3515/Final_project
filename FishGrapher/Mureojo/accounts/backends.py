from django.contrib.auth.backends import BaseBackend
from .models import User
import bcrypt

class MongoDBBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # Get user from MongoDB
            user = User.objects.get(username=username)

            # Verify password using bcrypt
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None