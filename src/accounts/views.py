from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

class AccountCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/account_create_form.html'
    success_message = '%(username)s user created!'
    
    def get_success_url(self):
        return reverse_lazy('accounts:account-login')

class AccountLoginView(LoginView):
    template_name = 'accounts/account_login_form.html'

class AccountLogoutView(LogoutView):
    template_name = 'accounts/account_post_logout.html'
