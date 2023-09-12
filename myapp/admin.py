from django.contrib import admin
from .models import Post, User, Bookmark

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Bookmark)
# Register your models here.
