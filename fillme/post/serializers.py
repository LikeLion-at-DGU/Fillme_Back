from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import *

# 댓글
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'writer', 'content', 'created_at', 'updated_at']
        
# 게시물
class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'       

