from django.urls import path
from . import views


app_name = 'fishBook'

urlpatterns = [
	path('book/', views.my_caught_fish_list, name='my_caught_fish_list'),
	# path('save_fish/', views.save_fish, name='save_fish'),
	path('search_fish/', views.search_fish, name='search_fish'),
]

