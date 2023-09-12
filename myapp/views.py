from django.db import IntegrityError
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from django.contrib.auth import authenticate, login, logout

from .serializers import UserSerializer, PostSerializer, BookmarkSerializer
from .models import User, Post, Bookmark
from .permissions import IsAuthorPermissions


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not(username and password):
            return Response({"error": "Передайте обов'язкові поля 'username' та 'password'"})

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Неправильний логін та/або пароль"})
        login(request, user)
        return Response({"message": f"{username}, ви успішно авторизовані"})


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Ви успішно вийшли з аккаунту"})


class UserView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorPermissions, IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class BookmarkView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).all()

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


class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not (username and password):
            return Response({"error": "Передайте обов'язкові поля 'username' та 'password'"})

        try:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
        except IntegrityError:
            return Response({"error": "Користувач з такою назвую вже існує "})

        else:
            return Response({"message": "Користувач успішно створенний "})




