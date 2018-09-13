from django.urls import path

from .views import (
    AccountCreateView,
    AccountLoginView, 
    AccountLogoutView,
    AccountPasswordResetConfirmView,
    AccountPasswordResetDoneView,
    AccountPasswordResetView,
    AccountProfileView,
    profile_edit,
)

app_name = 'accounts'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='account-create'),
    path('login/', AccountLoginView.as_view(), name='account-login'),
    path('logout/', AccountLogoutView.as_view(), name='account-logout'),
    path('password-reset/', AccountPasswordResetView.as_view(), name='account-password-reset'),
    path('password-reset/done/', AccountPasswordResetDoneView.as_view(), name='account-password-reset-done'),
    # path('password-reset-confirm/<uidb64>/<token>/', AccountPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('profile/', AccountProfileView.as_view(), name='account-profile'),
    path('profile/edit/', profile_edit, name='account-edit'),
]
