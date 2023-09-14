from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bookmarks = models.ManyToManyField(to="Post", through="Bookmark", through_fields=("user", "post"))


class Post(models.Model):
    id = models.AutoField(primary_key=True)

    content = models.CharField(max_length=2048, null=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, db_column="author_id", on_delete=models.CASCADE, related_name="posts")


class Bookmark(models.Model):

    id = models.AutoField(primary_key=True)

    post = models.ForeignKey(Post, db_column="post_id", on_delete=models.CASCADE)
    user = models.ForeignKey(User, db_column="user_id", on_delete=models.CASCADE)

