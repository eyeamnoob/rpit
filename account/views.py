from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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