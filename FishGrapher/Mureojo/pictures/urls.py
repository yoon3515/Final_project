from django.urls import path
from . import views

app_name = 'pictures'

urlpatterns = [
    path('save-image/', views.save_image, name='save-image'),
]
