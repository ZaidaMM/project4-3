from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Post(models.Model):
    user= models.ForeignKey("User", on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "body": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "user_id": self.user.id,
            "user_username": self.user.username,
            "like": self.like
        }

    def __str__(self):
        return f"{self.user.username}: {self.content} {self.timestamp}. Likes: {self.like}"

class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follows", default="")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed", default="")

    def __str__(self):
        return f"{self.follower} follows {self.followed}"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_liked", default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_liked", default="")

    def __str__(self):
        return f"{self.user} liked {self.post}"
