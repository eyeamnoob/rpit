# from django.shortcuts import render
from api.serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from post.models import Post
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class PostListCreateAPIVeiw(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        obj = self.get_serializer(data=request.data)
        if obj.is_valid():
            obj.save(user=self.request.user)
            self.get_success_headers(obj.data)
            return Response(obj.data, status=status.HTTP_201_CREATED, headers=self.get_success_headers(obj.data))
        return Response(data=obj.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
