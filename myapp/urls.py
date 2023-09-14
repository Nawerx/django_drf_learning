from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
from .views import (
    UserView,
    #PostView,
    #PostDetailView,
    BookmarkView,
    LoginView,
    LogoutView,
    SignupView,
    PostViewSet)

router.register("posts", PostViewSet)
urlpatterns = [
    path('users/', UserView.as_view()),
    # path('posts/', PostView.as_view()),
    # path("posts/<int:pk>", PostViewSet.as_view({"get": "retrieve"})), #retrieve - посмотреть одно 1 что-то
    # path("posts/", PostViewSet.as_view({"get": "list"})),
    path("", include(router.urls)),
    path("bookmarks/", BookmarkView.as_view()),
    path("auth/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("signup/", SignupView.as_view()),
]


