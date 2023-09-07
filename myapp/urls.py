from django.urls import path
from .views import UserView, PostView, PostDetailView, BookmarkView, LoginView, LogoutView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('posts/', PostView.as_view()),
    path("posts/<int:pk>", PostDetailView.as_view()),
    path("bookmarks/", BookmarkView.as_view()),
    path("auth/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
]
