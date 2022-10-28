from rest_framework import serializers
from .models import (Post,
                     Comment,
                     PostLike,
                     CommentLike)
from django.contrib.auth.models import User

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
