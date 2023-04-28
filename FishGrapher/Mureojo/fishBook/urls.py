from django.urls import path
from . import views


app_name = 'fishBook'

urlpatterns = [
	path('', views.my_caught_fish_list, name='my_caught_fish_list'),
	path('book_result/', views.search_fish, name='search_fish'),
]

