from django.urls import path

from .views import (
    AccountCreateView, 
    AccountLoginView, 
    AccountLogoutView
)

app_name = 'accounts'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='account-create'),
    path('login/', AccountLoginView.as_view(), name='account-login'),
    path('logout/', AccountLogoutView.as_view(), name='account-logout'),
]
