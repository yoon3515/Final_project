from django.urls import path
from . import views


app_name = 'fishBook'

urlpatterns = [
	path('', views.fish_book_list, name='fish_book_list'),
	path('save_fish_book/', views.save_fish_book, name='save_fish_book'),
]

