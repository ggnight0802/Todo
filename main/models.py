from django.db import models

# Create your models here.


class Todo(models.Model):
    Todo_id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Todo_comment(models.Model):
    Todo_comment_id = models.AutoField(primary_key=True)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contents