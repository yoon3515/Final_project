from django.urls import path

from . import views

app_name = 'map'  # namespace 추가

urlpatterns = [
    path('', views.show_map, name='show_map'),
]
