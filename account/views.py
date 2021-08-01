from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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


class Registration(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy("account:panel")
