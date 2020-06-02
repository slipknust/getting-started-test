from django.contrib import admin

# Register your models here.

from hello.models import Post

admin.site.register(Post)