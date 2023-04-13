from django.urls import path

from . import views

app_name = "login"

urlpatterns = [
    path("", views.index, name="login"),
    path("register/", views.index, name="register"),
    path("find/", views.index, name="find"),
]