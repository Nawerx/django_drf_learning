from django.urls import path
from .views import UserView, PostView, PostDetailView, BookmarkView

urlpatterns = [
    path('users/', UserView.as_view()),
    # path('posts/', PostView.as_view()),
    path("posts/<int:pk>", PostDetailView.as_view()),
    path("bookmarks/", BookmarkView.as_view())
]
