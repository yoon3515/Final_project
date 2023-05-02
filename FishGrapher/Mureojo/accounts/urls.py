from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('signup/', views.signup, name='signup'),
  path('id', views.RecoverIdView.as_view(), name='id'),
  path('id/find', views.ajax_find_id_view, name='ajax_id')
  # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
  # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
  # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
