from django.urls import path

from .views import (
    AccountCreateView,
    AccountLoginView, 
    AccountLogoutView,
    AccountProfileView,
    AccountUpdateView,
    # profile_edit,
)

app_name = 'accounts'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='account-create'),
    path('login/', AccountLoginView.as_view(), name='account-login'),
    path('logout/', AccountLogoutView.as_view(), name='account-logout'),
    path('profile/', AccountProfileView.as_view(), name='account-profile'),
    path('profile/edit/', AccountUpdateView.as_view(), name='account-edit'),
]
