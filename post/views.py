from tkinter.messagebox import RETRY
from urllib import response
from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from notice.serializers import *
from accounts.models import *
from mypage.models import *
from .models import Post, Comment
from .serializers import *

# Create your views here.

# POST(게시물) 관련
# 1. 모든 게시물 가져 오기 및 사진 게시물 작성(로그인만 하면 유저 제한 없음)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list_create(request):
    user = request.user

    if request.method == 'GET':
        request.data['writer'] = user.id #작성자의 id값을 저장하는 코드
        posts = Post.objects.all()
        serializer = AllPostSerializer(posts, many = True)

        return Response(data = serializer.data)

    if request.method == 'POST':
        if Persona.objects.get(pk=request.data['persona']).user == user:
            request.data['writer'] = user.id
            serializer = PostSerializer(data = request.data)

            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response(data = serializer.data)
        else:
            return Response({"warning":"본인의 페르소나가 아닙니다."})

# 2. 사진 - 특정 게시물 가져 오기 / 수정 / 삭제(게시물 작성한 유저만 수정, 삭제 가능하게)
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
            if Persona.objects.get(pk=request.data['persona']).user == user:
                request.data['writer'] = user.id
                serializer = PostSerializer(instance = post, data = request.data)
                if serializer.is_valid(raise_exception = True):
                    serializer.save()
                return Response(serializer.data)
            else:
                return Response({"warning":"본인의 페르소나가 아닙니다."})
        else:
            return Response({"warning":"본인의 게시글이 아닙니다."})

    elif request.method == 'DELETE':
        if user == post.writer:
            post.delete()
            data = {
                'post':post_pk
            }
            return Response(data)

# 3. 영상 - 특정 게시물 작성하기
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def video_post_create(request):
    user = request.user

    if request.method == 'POST':
        if Persona.objects.get(pk=request.data['persona']).user == user:
            request.data['writer'] = user.id
            serializer = VideoSerializer(data = request.data)

            if serializer.is_valid(raise_exception = True):
                serializer.save()
                return Response(data = serializer.data)
        else:
            return Response({"warning":"본인의 페르소나가 아닙니다."})

# 4. 영상 - 특정 게시물 가져 오기 / 수정 / 삭제(게시물 작성한 유저만 수정, 삭제 가능하게)
@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def video_post_update_delete(request, post_pk):
    user = request.user
    post = get_object_or_404(Post, pk = post_pk)

    if request.method == 'GET':
        request.data['writer'] = user.id
        serializer = VideoSerializer(post)
        return Response(serializer.data)

    if request.method == 'PATCH':
        if user == post.writer:
            if Persona.objects.get(pk=request.data['persona']).user == user:
                request.data['writer'] = user.id
                serializer = VideoSerializer(instance = post, data = request.data)
                if serializer.is_valid(raise_exception = True):
                    serializer.save()
                return Response(serializer.data)
            else:
                return Response({"warning":"본인의 페르소나가 아닙니다."})
        else:
            return Response({"warning":"본인의 게시글이 아닙니다."})

    elif request.method == 'DELETE':
        if user == post.writer:
            post.delete()
            data = {
                'post':post_pk
            }
            return Response(data)

# 0817 추가
# 1. 내가 팔로우한 유저의 게시글만 조회가능한 api
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def following_post_list(request):
    user = request.user # 로그인한 유저(= 나) 정보 불러 오기
    followings = user.profile.followings.all() # 내가 팔로우한 유저들 불러 오기
    postList = []

    if request.method == 'GET':
        for following in followings:
            posts = Post.objects.filter(writer = following.user)
            followingPost = AllPostSerializer(posts, many = True)
            postData = list(followingPost.data)
            for data in postData:
                postList.append(data)
        serializer = sorted(postList, key = lambda k: k.get('created_at',0), reverse = True)
        return Response(serializer)

# 2. 내가 작성한 게시글 목록을 조회하는 api
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_post_list(request):
    user = request.user # 로그인한 유저(= 나) 정보 불러 오기

    if request.method == 'GET':
        request.data['writer'] = user.id # 해당 게시물의 writer는 user.id의 값을 입력 이런 의미인 것 같은데?
        posts = Post.objects.filter(writer = user)
        serializer = AllPostSerializer(posts, many = True)
        return Response(serializer.data)

# 3. 나의 특정 페르소나가 작성한 게시글 목록을 조회하는 api
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def my_persona_post_list(request, persona_id):
    user = request.user
    persona = get_object_or_404(Persona, pk = persona_id)
    post = Post.objects.filter(persona=persona) 

    if request.method == 'GET':
        request.data['writer'] = user.id
        # posts = Post.objects.filter(persona = persona)
        serializer = AllPostSerializer(post, many = True)
        return Response(serializer.data)

# 4. 내가 아닌 특정 유저가 작성한 게시글만 조회하는 api
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_post_list(request, user_id):
    user = User.objects.get(pk = user_id)

    if request.method == 'GET':
        request.data['writer'] = user.id
        posts = Post.objects.filter(writer = user)
        serializer = AllPostSerializer(posts, many = True)
        return Response(serializer.data)

# 5. 내가 아닌 특정 유저의 특정 페르소나가 작성한 게시글만 조회하는 api
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_persona_post_list(request, user_id, persona_id):
    user = get_object_or_404(User, pk = user_id) # 유저 한 번 거르고 -> 특정 유저
    persona = get_object_or_404(Persona, pk = persona_id)
    post = Post.objects.filter(persona = persona) 

    if request.method == 'GET':
        request.data['writer'] = user.id
        serializer = AllPostSerializer(post, many = True)
        return Response(serializer.data)

# 6. 내가 소식받기한 페르소나의 게시글만 조회하는 api
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def subfollowing_post_list(request):
    fillme = User.objects.get(username = "fillmeofficial")
    user = request.user # 로그인한 유저(= 나) 정보 불러 오기
    subfollowings = user.profile.subfollowings.all() # 내가 팔로우한 유저들 불러 오기
    # persona = get_object_or_404(Persona, pk = persona_id)    
    postList = []
    is_follower = user.profile in fillme.profile.followers.all()
    if request.method == 'GET':
        for subfollowing in subfollowings:
                posts = Post.objects.filter(persona = subfollowing)
                followingPost = AllPostSerializer(posts, many = True)
                postData = list(followingPost.data)
                if subfollowing.openpublic == True:
                    for data in postData:
                        postList.append(data)
        myposts = Post.objects.filter(writer = user)
        myPost = AllPostSerializer(myposts, many=True)
        mypostData = list(myPost.data)
        for data in mypostData:
            postList.append(data)
        if not is_follower:
            fillmeposts = Post.objects.filter(writer = fillme)
            fillmepost = AllPostSerializer(fillmeposts, many=True)
            fillmedata = list(fillmepost.data)
            for data in fillmedata:
                postList.append(data)
        serializer = sorted(postList, key = lambda k: k.get('created_at',0), reverse = True)
        return Response(serializer)


# COMMENT(댓글) 관련
# 1. 특정 게시물의 댓글 보기 / 작성하기
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_comment_list(request, post_id):
    user = request.user
    post = Post.objects.get(pk = post_id)

    if request.method == 'GET':
        comments = Comment.objects.filter(post = post_id)
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CommentcreateSerializer(data = {
            "writer" : user.id,
            "post": post.id,
            "content":request.data["content"]
            })
        notice = NoticeSerializer(data={
                "user":post.writer.id,
                "userfrom":user.username,
                "userto":post.persona.name,
                "text":"님의 게시글에 댓글을 남겼습니다.",
                "content":request.data["content"]
            })
        if notice.is_valid():
            notice.save()
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
            notice = NoticeSerializer(data={
                "user":post_like.writer.id,
                "userfrom":request.user.username,
                "userto":post_like.persona.name,
                "text":"님의 게시물을 좋아합니다.",
                "content":"null"
            })
            if notice.is_valid():
                notice.save()
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(data = serializer.data)