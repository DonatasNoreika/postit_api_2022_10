from rest_framework import serializers
from .models import (Post,
                     Comment,
                     PostLike,
                     CommentLike)


class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'user_id', 'user', 'created']
