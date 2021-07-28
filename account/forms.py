from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "لقب یا گذرواژه معتبر نیست",
        'inactive': "این یک حساب فعال نیست",
    }

    password = forms.CharField(
        label="گذرواژه",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )