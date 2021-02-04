from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Todo,Todo_comment
from .serializers import TodoSerializer,TodoCommentSerializer

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'Todo_id'

class TodoCommentList(generics.ListCreateAPIView):
    queryset = Todo_comment.objects.all()
    serializer_class = TodoCommentSerializer

class TodoCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo_comment.objects.all()
    serializer_class = TodoCommentSerializer
    lookup_field = 'Todo_comment_id'