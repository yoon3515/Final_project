from django.urls import path
from . import views
from .views import edit_profile

app_name = 'mypage'
urlpatterns = [
    path("", views.mypage, name='showinfo'),
    # path("modify/", views.modify, name='modify'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('modify-pw/', views.modify_pw, name='modify_pw'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
]