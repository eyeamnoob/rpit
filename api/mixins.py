from rest_framework import status
from rest_framework.response import Response


class AutoSetUserMixin:
    def create(self, request, *args, **kwargs):
        obj = self.get_serializer(data=request.data)
        obj.is_valid(raise_exception=True)
        print(obj.validated_data["title"])
        obj.validated_data["user"] = request.user
        obj.save()
        return Response(obj.data, status=status.HTTP_201_CREATED)