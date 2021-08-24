from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserModel
from django import forms
from django.contrib.auth import get_user_model, password_validation, authenticate
from django.core.exceptions import ValidationError


class CustomAuthenticationForm(forms.Form):
    error_messages = {
        'invalid_login': "ایمیل یا گذرواژه معتبر نیست",
        'inactive': "این حساب فعال نیست",
    }

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.TextInput(attrs={"autofocus": True}),
        max_length=150
    )
    password = forms.CharField(
        label="گذرواژه",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'})
    )
    remember_me = forms.BooleanField(required=False)

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email is not None and password:
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                raise self.get_invalid_login_error()
            self.user_cache = authenticate(self.request, username=user.get_username(), password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
    
    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': UserModel._meta.get_field(UserModel.EMAIL_FIELD)},
        )
    
    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache


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

