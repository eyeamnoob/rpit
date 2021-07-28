from django.urls import path
from .views import CustomLoginView, UserPanelView, CustomLogoutView

app_name = "account"

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('panel/', UserPanelView.as_view(), name='panel'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]