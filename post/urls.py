from . import views as my_view
from django.urls import path

app_name = "post"

urlpatterns = [
    path("list/", my_view.PostListView.as_view(), name='post_list'),
    path("detail/<int:pk>/", my_view.PostDetailView.as_view(), name='post_detail'),
]