from rest_framework import serializers
from .models import (Post,
                     Comment,
                     PostLike,
                     CommentLike)

class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_id', 'post', 'body', 'created']

class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user = serializers.ReadOnlyField(source='user.username')
    # comments = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()
    comments = serializers.StringRelatedField(many=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'user_id', 'user', 'created', 'comment_count', 'comments', 'likes', 'image']

    def get_comment_count(self, post):
        return Comment.objects.filter(post=post).count()

    def get_likes(self, post):
        return PostLike.objects.filter(post=post).count()

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id']