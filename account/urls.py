from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    # Other authentication URLs
    path("password-change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # User management
    path("register/", views.register, name="register"),
    path("edit/", views.edit, name="edit"),
    path("users/", views.user_list, name="user_list"),
    path("users/<username>/", views.user_detail, name="user_detail"),
    path("verify-email/<str:token>/", views.verify_email, name="verify_email"),
    path("verification-sent/", views.verification_sent, name="verification_sent"),
    path("follow/<str:username>/", views.follow_user, name="follow_user"),
    path("unfollow/<str:username>/", views.unfollow_user, name="unfollow_user"),
]
