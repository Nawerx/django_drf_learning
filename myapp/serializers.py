from rest_framework import serializers
from .models import User, Post, Bookmark


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bookmarks"]


class PostSerializer(serializers.ModelSerializer):
    author = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    bookmarks = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "bookmarks"]


class BookmarkSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Bookmark
        fields = ["id", "post"]