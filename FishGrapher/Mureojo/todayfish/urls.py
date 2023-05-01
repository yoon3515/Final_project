from django.urls import path
from . import views

app_name = 'todayfish'

urlpatterns = [
    path('?result=/', views.save_image, name='save-image'),
]
