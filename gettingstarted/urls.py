from django.urls import path, include

from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("lucasteste/", hello.views.lucasteste, name="lucasteste"),
    path("list/", hello.views.list, name="list"),
    path("list/task/<int:id>", hello.views.taskView, name="task"),
    path("videos/", hello.views.videos, name="videos"),
    path("pessoa/", hello.views.pessoa, name="pessoa"),
    path("newPessoa/", hello.views.newPessoa, name="new-pessoa"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
