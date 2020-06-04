from django.contrib import admin

# Register your models here.

from hello.models import Post, Hello

admin.site.register(Post)
admin.site.register(Hello)