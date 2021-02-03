from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('todos',views.TodoList.as_view()),
    path('todos/<int:pk>/',views.TodoDetail.as_view()),
    path('todos/<int:pk>/comments',views.TodoCommentList.as_view()),
    path('todos/<int:pk>/comments/<int:pk_alt>/',views.TodoCommentDetail.as_view()),
]