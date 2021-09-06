# from django.shortcuts import render
from api.serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView
from post.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class PostListAPIVeiw(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer