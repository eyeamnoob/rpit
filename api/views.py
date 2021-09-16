# from django.shortcuts import render
from rest_framework.response import Response
from api.serializers import CommentSerializer, PostSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from post.models import Comment, Post
from . import mixins as my_mixins

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