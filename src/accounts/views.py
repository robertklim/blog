from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    LoginView, 
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, 
    DetailView,
    UpdateView, 
    View,
)

from .forms import (
    AccountCreateForm,
    AccountUpdateForm,
    ProfileUpdateForm,
)

from .models import Profile

class AccountCreateView(SuccessMessageMixin, CreateView):
    form_class = AccountCreateForm
    template_name = 'accounts/account_create_form.html'
    success_message = '%(username)s user created!'
    
    def get_success_url(self):
        return reverse_lazy('accounts:account-login')

class AccountProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/account_profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class AccountLoginView(LoginView):
    template_name = 'accounts/account_login_form.html'

class AccountLogoutView(LogoutView):
    template_name = 'accounts/account_post_logout.html'

class AccountPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

class AccountPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'

class AccountPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class AccountPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'

@login_required
def profile_edit(request):
    if request.method == 'POST':
        acc_form = AccountUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)
        if acc_form.is_valid() and prof_form.is_valid():
            acc_form.save()
            prof_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('accounts:account-profile')
    else:
        acc_form = AccountUpdateForm(instance=request.user)
        prof_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'acc_form': acc_form,
        'prof_form': prof_form,
    }

    return render(request, 'accounts/account_update_form.html', context)

