from django.urls import path
from . import views


app_name = 'fish_info'

urlpatterns = [
    path('<int:fish_id>/', views.fish_info, name='fish_info'),
]

