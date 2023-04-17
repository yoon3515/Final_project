from django.urls import path, include
from accounts.views import google_login, google_callback, GoogleLogin

app_name = "accounts"

urlpatterns = [
    path('google/login', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
    path('google/login/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
]
