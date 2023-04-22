from . import views
from django.urls import path


app_name = 'accounts'

urlpatterns = [
  path('login/', views.CustomLogin, name='login'),
  path('logout/', views.CustomLogout, name='logout'),
  path('signup/', views.CustomSignup, name='signup')
]
