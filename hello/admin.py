from django.contrib import admin

# Register your models here.

from hello.models import Post, Hello, Video, Pessoa

admin.site.register(Post)
admin.site.register(Hello)
admin.site.register(Video)
admin.site.register(Pessoa)