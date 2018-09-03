from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

class AccountCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/account_create_form.html'
    
    def get_success_url(self):
        return reverse_lazy('accounts:account-login')

class AccountLoginView(LoginView):
    template_name = 'accounts/account_login_form.html'
