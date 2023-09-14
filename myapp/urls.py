from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
from .views import (
    UserView,
    BookmarkView,
    LoginView,
    LogoutView,
    SignupView,
    PostViewSet, UserViewSet)

router.register("posts", PostViewSet)
router.register("users", UserViewSet)

urlpatterns = [
    # path('users/', UserViewSet.as_view()),
    # path("posts/<int:pk>", PostViewSet.as_view({"get": "retrieve"})), #retrieve - посмотреть одно 1 что-то
    path("", include(router.urls)),
    path("bookmarks/", BookmarkView.as_view()),
    path("auth/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("signup/", SignupView.as_view()),
]


