from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Post(models.Model):
    user= models.ForeignKey("User", on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "body": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "user_id": self.user.id,
            "user_username": self.user.username
        }

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"