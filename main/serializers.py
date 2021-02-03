from rest_framework import serializers
from . import models


class TodoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ('Todo_id','title','description','is_completed','created_at','updated_at',)
        model = models.Todo


class TodoCommentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        fields = ('Todo_comment_id','contents','created_at','updated_at')
        model = models.Todo_comment