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
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'user_id', 'user', 'created', 'comments']


