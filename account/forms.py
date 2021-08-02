from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth import get_user_model, password_validation

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "لقب یا گذرواژه معتبر نیست",
        'inactive': "این حساب فعال نیست",
    }

    password = forms.CharField(
        label="گذرواژه",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "گذرواژه ها مطابقت ندارند",
        'password_too_similar': "شبیه است"
    }

    password1 = forms.CharField(
        label="گذرواژه",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="تکرار گذرواژه",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="گذرواژه خود را دوباره وارد کنید",
    )

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

