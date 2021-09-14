from post.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    def get_author_username(self, obj):
        return obj.user.username
    
    user = serializers.SerializerMethodField("get_author_username")

    class Meta:
        model = Post
        fields = '__all__'
