from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer, LikeSerializer, PostLikeSerializer

# Create your views here.

# POST(게시물) 관련
# 1. 모든 게시물 가져 오기 및 게시물 작성(로그인만 하면 유저 제한 없음)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list_create(request):
    user = request.user

    if request.method == 'GET':
        request.data['writer'] = user.id
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)

        return Response(data = serializer.data)

    if request.method == 'POST':
        request.data['writer'] = user.id
        serializer = PostSerializer(data = request.data)

        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(data = serializer.data)

# 2. 특정 게시물 가져 오기 / 수정 / 삭제(게시물 작성한 유저만 수정, 삭제 가능하게)
@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail_update_delete(request, post_pk):
    user = request.user
    post = get_object_or_404(Post, pk = post_pk)

    if request.method == 'GET':
        request.data['writer'] = user.id
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        if user == post.writer:
            request.data['writer'] = user.id
            serializer = PostSerializer(instance = post, data = request.data)
            if serializer.is_valid(raise_exception = True):
                serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        if user == post.writer:
            post.delete()
            data = {
                'post':post_pk
            }
            return Response(data)


# COMMENT(댓글) 관련
# 1. 특정 게시물의 댓글 보기 / 작성하기
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_comment_list(request, post_id):
    user = request.user
    post = Post.objects.get(pk = post_id)

    if request.method == 'GET':
        request.data['writer'] = user.id
        request.data['post'] = post.id
        comments = Comment.objects.filter(post = post_id)
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        request.data['writer'] = user.id
        request.data['post'] = post.id
        serializer = CommentSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

# 2. 특정 게시물의 특정 댓글 보기 / 수정 / 삭제
@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_comment_detail_update_delete(request, post_pk, comment_pk):
    user = request.user # 로그인한 유저 정보
    post = get_object_or_404(Post, pk = post_pk)
    comment = get_object_or_404(Comment.objects.filter(post = post_pk), pk = comment_pk)

    if request.method == 'GET':
        request.data['writer'] = user.id
        request.data['post'] = post.id
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PATCH': # 자신의 댓글만 수정 가능 / 타인의 댓글은 수정 불가능
        if user == comment.writer:
            request.data['writer'] = user.id
            request.data['post'] = post.id
            serializer = CommentSerializer(instance = comment, data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(post = post) # 해당 글에 댓글 쓰기
            return Response(serializer.data)

    elif request.method == 'DELETE': # 자신의 게시물 속 댓글은 모두 삭제 가능(타인의 것이라도)
        if user == comment.writer or user == post.writer:
            comment.delete()
            return Response({'comment':comment_pk})

# 좋아요 관련
# 1. 해당 게시물 좋아요 수 보기
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_likes(request, post_pk):
    post = get_object_or_404(Post, pk = post_pk) # 해당 게시물
    serializer = PostLikeSerializer(post)
    return Response(data = serializer.data)

# 2. 해당 게시물 속 좋아요 누르기 / 취소하기
@api_view(['PATCH'])
@permission_classes([IsAuthenticatedOrReadOnly])
def send_like(request, post_pk):
    post_like = get_object_or_404(Post, pk = post_pk)
    num = post_like.like_num

    if request.method == 'PATCH':

        if request.user in post_like.liked_user.all():
            post_like.liked_user.remove(request.user)
            num = num - 1
            request.data['like_num'] = num
            if num < 0:
                num = 0
            post_like.save()
            serializer = LikeSerializer(instance=post_like, data ={"persona":post_like.persona.id, "title":post_like.title, "content":post_like.content, 'like_num':num})

            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(data = serializer.data)

        else:
            post_like.liked_user.add(request.user)
            num = num + 1
            request.data['like_num'] = num
            if num < 0:
                num = 0
            post_like.save()
            serializer = LikeSerializer(instance=post_like, data ={"persona":post_like.persona.id, "title":post_like.title, "content":post_like.content, 'like_num':num})

            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(data = serializer.data)