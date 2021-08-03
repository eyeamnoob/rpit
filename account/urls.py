from unicodedata import name
from django.urls import path
from . import views as my_view

app_name = "account"

urlpatterns = [
    path('login/', my_view.CustomLoginView.as_view(), name='login'),
    path('panel/', my_view.UserPanelView.as_view(), name='panel'),
    path('logout/', my_view.CustomLogoutView.as_view(), name='logout'),
    path('registration/', my_view.RegistrationView.as_view(), name='registration'),
    
    # auth app spawword reset
    path('password-reset/', my_view.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset_done/', my_view.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', my_view.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', my_view.CustomPasswordResetCompleteVeiw.as_view(), name='password_reset_complete'),
]