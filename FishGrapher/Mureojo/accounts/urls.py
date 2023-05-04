from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('signup/', views.signup, name='signup'),
  path('recover/id/', views.RecoverIdView.as_view(), name='recover_id'),
  path('recover/id/find/', views.ajax_find_id_view, name='ajax_id'),
  path('recover/pw/', views.RecoverPwView.as_view(), name='recover_pw'),
  path('recover/pw/find/', views.ajax_find_pw_view, name='ajax_pw'),
  path('recover/pw/auth/', views.auth_confirm_view, name='recover_auth'),
  path('recover/pw/reset/', views.auth_pw_reset_view, name='recover_pw_reset'),

]
