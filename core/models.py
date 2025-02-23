from django.contrib.auth import get_user_model
from django.db import models

import uuid


User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(max_length=400, blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.user.username
    

class LikePost(models.Model):
    post_id = models.CharField(max_length=255)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class FollowUser(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='+')
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.username
