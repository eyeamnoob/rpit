# from django.shortcuts import render
from api.serializers import PostSerializer
from rest_framework.generics import ListAPIView
from post.models import Post

# Create your views here.

class PostListAPIVeiw(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer