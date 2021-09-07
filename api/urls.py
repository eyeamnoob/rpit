from django.urls import path
from . import views as my_view
from rest_framework.authtoken.views import obtain_auth_token

app_name = "api"

urlpatterns = [
    path('post/list/', my_view.PostListAPIVeiw.as_view(), name="post_list"),
    path('obtain-token/', obtain_auth_token, name='obtain_token'),
    path('post/retrieve/<int:pk>/', my_view.PostRetrieveUpdateDestroyAPIView.as_view(), name='post_retrieve'),
]
