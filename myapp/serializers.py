from rest_framework import serializers
from .models import User, Post, Bookmark


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class SimplePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "content", "updated_at", "created_at"]


class PostSerializer(serializers.ModelSerializer):
    author = SimpleUserSerializer(read_only=True)


    class Meta:
        model = Post
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    bookmarks = PostSerializer(many=True)
    posts = SimplePostSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "bookmarks", "posts"]


class BookmarkSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Bookmark
        fields = ["id", "post"]