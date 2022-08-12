from django.urls import path
from .views import *
from . import views

app_name = "post"
urlpatterns = [
    path('', post_list_create, name = 'post_list_create'), # 모든 게시물 가져 오기 및 게시물 작성
    path('<int:post_pk>/', post_detail_update_delete, name = 'post_detail_update_delete'), # 특정 게시물 가져 오기 / 수정 / 삭제
    path('comments/', comment_list, name = "comment_list"), # 모든 댓글 리스트 가져 오기
    path('<int:post_id>/comments/', post_comment_list, name = 'post_comment_list'), # 특정 게시물의 댓글 보기 / 작성하기
    path('<int:post_pk>/comments/<int:comment_pk>/', post_comment_detail_update_delete, name = 'post_comment_detail_update_delete'), # 특정 게시물의 특정 댓글 보기 / 수정 / 삭제
]