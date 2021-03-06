from django.urls import path
from . import views as my_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "api"

urlpatterns = [
    path('post/list/', my_view.PostListCreateAPIVeiw.as_view(), name="post_list"),
    path('post/retrieve/<int:pk>/', my_view.PostRetrieveUpdateDestroyAPIView.as_view(), name='post_retrieve'),
    path('comment/list/', my_view.CommentListCreateAPIView.as_view(), name='comment_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('like-dislike/<int:pk>/', my_view.LikeActivityAPIView.as_view(), name='like_activity'),
]
