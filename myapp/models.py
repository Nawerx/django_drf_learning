from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bookmarks = models.ManyToManyField(
        to="Post", through="Bookmark", through_fields=("user", "post")
    )
    followers = models.ManyToManyField(
        to="self",
        symmetrical=False,
        through="SubscriberItems",
        through_fields=("user", "follower"),
        related_name="following",
    )


class SubscriberItems(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="sub_items_followers",
    )
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="follower_id",
        related_name="sub_items_following",
    )

    class Meta:
        db_table = "SubscriberItems"


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
