from django import template
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import (PasswordResetView,
                                        PasswordResetDoneView,
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView)

# Create your views here.


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args: str, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("account:panel")
        return super().get(request, *args, **kwargs)


class UserPanelView(LoginRequiredMixin, TemplateView):
    template_name = 'user_panel.html'


class CustomLogoutView(LogoutView):
    template_name = 'logout.html'


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy("account:panel")


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('account:password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')


class CustomPasswordResetCompleteVeiw(PasswordResetCompleteView):
    template_name = ('password_reset_complete.html')