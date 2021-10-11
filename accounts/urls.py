from django.urls import path
from .views import PasswordsChangeView,UserEditView
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('success/', views.succesmessage, name='success_message'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password/', PasswordsChangeView.as_view(template_name='accounts/change-password.html'), name='change_password'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    
    path('password_reset/',
    auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
     name='password_reset'),

    path('password_reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
     name='password_reset_confirm'),

    path('reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
     name='password_reset_complete'),
]
 