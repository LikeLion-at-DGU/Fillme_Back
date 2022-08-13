from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import *

# 게시물
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'       

# 댓글
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'writer', 'content', 'created_at', 'updated_at']