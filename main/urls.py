from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('todos',views.TodoList.as_view()),
    path('todos/<int:Todo_id>/',views.TodoDetail.as_view()),
    path('todos/<int:Todo_id>/comments',views.TodoCommentList.as_view()),
    path('todos/<int:Todo_id>/comments/<int:Todo_comment_id>/',views.TodoCommentDetail.as_view()),
]