# from django.shortcuts import render
from rest_framework.response import Response
from .serializers import CommentSerializer, LikeActivitySeriallizer, PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from post.models import Comment, LikeActivity, Post
from . import mixins as my_mixins
from rest_framework import status

# Create your views here.

class PostListCreateAPIVeiw(my_mixins.AutoSetUserMixin, ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListCreateAPIView(my_mixins.AutoFillCommentFieldsMixin, ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeActivityAPIView(GenericAPIView):
    serializer_class = LikeActivitySeriallizer
    def post(self, request, *args, **kwargs):
        try:
            la = LikeActivity.objects.get(user=request.user, post__id=kwargs['pk'])
        except LikeActivity.DoesNotExist:
            if request.data['action'] == 'like':
                post = Post.objects.get(pk=kwargs['pk'])
                LikeActivity.objects.create(user=request.user, post=post)
                return Response(status=status.HTTP_201_CREATED)
        if request.data['action'] == 'dislike':
            la.delete()
            return Response(status=status.HTTP_201_CREATED)
        return Response({"detail": "مطمعن شوید پستی با این شناسه وجود دارد. یک پست را دوبار لایک یا دیسلایک نکنید"}, status=status.HTTP_400_BAD_REQUEST)