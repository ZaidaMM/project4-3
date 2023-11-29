from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Post(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name='posts')
    body = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "author": self.author,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "author_id": self.author.id,
            "author_username": self.author.user.username
        }
