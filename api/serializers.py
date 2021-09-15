from post.models import Post, Comment
from rest_framework import serializers
from . import mixins as my_mixins


class PostSerializer(my_mixins.SerializerMethodMixin, serializers.ModelSerializer):
    user = serializers.SerializerMethodField("get_user_username")

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(my_mixins.SerializerMethodMixin, serializers.ModelSerializer):
    def get_post_title(self, obj):
        return obj.post.title
    
    def get_reply_to_body(self, obj):
        if obj.reply_to:
            return obj.reply_to.body

    user = serializers.SerializerMethodField('get_user_username')
    post = serializers.SerializerMethodField('get_post_title')
    reply_to = serializers.SerializerMethodField('get_reply_to_body')

    class Meta:
        model = Comment
        fields = '__all__'