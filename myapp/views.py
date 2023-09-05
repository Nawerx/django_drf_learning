from django.db import IntegrityError
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, PostSerializer, BookmarkSerializer
from .models import User, Post, Bookmark


class UserView(ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()


# class PostView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request):
#         posts = Post.objects.all().values()
#         return Response({"posts": list(posts)})
#
#     def post(self, request):
#         new_post = Post.objects.create(
#             content=request.data["content"],
#             author_id=request.data["author"]
#         )
#         return Response({"posts": model_to_dict(new_post)})

class PostView(ListCreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class BookmarkView(ListCreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def post(self, request, *args, **kwargs):
        post_id = request.data["post"]
        user_id = request.data["user"]
        try:
            bookmark = Bookmark.objects.filter(post_id=post_id, user_id=user_id).all()

            if not bookmark:
                new_bookmark = Bookmark.objects.create(post_id=post_id, user_id=user_id)
                return Response(model_to_dict(new_bookmark))

            return Response("Така замітка вже існує")

        except IntegrityError:
            return Response("Такого користувача або замітки не існує")







