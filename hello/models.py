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