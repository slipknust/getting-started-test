from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField(null=True)
    content = RichTextUploadingField(null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    created_at = models.DateField(auto_now_add=True)

class Hello(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)
    sexo = models.CharField(max_length=20)
    genMusicFav = models.CharField(max_length=255)