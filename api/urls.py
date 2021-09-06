from django.urls import path
from . import views as my_view
app_name = "api"

urlpatterns = [
    path('post/list/', my_view.PostListAPIVeiw.as_view(), name="post_list"),
]
