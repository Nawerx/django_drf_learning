from django.contrib import admin
from .models import Post, User, Bookmark, SubscriberItems

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Bookmark)
admin.site.register(SubscriberItems)
# Register your models here.
