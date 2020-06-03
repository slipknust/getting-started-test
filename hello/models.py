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
        (1, 'Doing'),
        (2, 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=1,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

