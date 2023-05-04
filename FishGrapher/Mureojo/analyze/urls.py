from django.urls import path
from . import views

app_name = 'analyze'

urlpatterns = [
    path('camera/', views.analyze, name='camera'),
    path('todayfish/', views.today_fish, name='todayfish'),
]
