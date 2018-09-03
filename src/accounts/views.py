from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView

class AccountCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/account_create_form.html'
    success_url = '/'
