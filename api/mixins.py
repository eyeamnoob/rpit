from django.http.response import Http404
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from post.models import Comment, Post


class AutoSetUserMixin:
    def create(self, request, *args, **kwargs):
        obj = self.get_serializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.validated_data["user"] = request.user
        obj.save()
        return Response(obj.data, status=status.HTTP_201_CREATED)


class SerializerMethodMixin:
    def get_username(self, obj):
        return obj.user.username


class AutoFillCommentFieldsMixin:
    def create(self, request, *args, **kwargs):
        obj = self.get_serializer(data=request.data)
        obj.is_valid(raise_exception=True)
        if request.data.get('post') is None:
            raise Http404('پست مورد نظر پیدا نشد')
        post = get_object_or_404(Post, pk=int(request.data.get('post')))
        if request.data.get('reply_to') is not None:
            reply_to = get_object_or_404(Comment, pk=int(request.data.get('reply_to')))
            if reply_to.post.id != post.pk:
                return Response("نمیتوان از پستی، جواب یک کامنت در پست دیگری را داد", status=status.HTTP_400_BAD_REQUEST)
            obj.validated_data['reply_to'] = reply_to
        obj.validated_data['post'] = post
        obj.validated_data['user'] = request.user
        obj.save()
        return Response(obj.data, status=status.HTTP_201_CREATED)