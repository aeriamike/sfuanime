from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models

from django.utils import timezone
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from tinymce_4.fields import TinyMCEModelField





class Posts(models.Model):

    post_title  = models.CharField(max_length=200)
    post_content  = models.TextField(blank = True, null = True)
    post_date = models.DateTimeField()
    post_tag = ArrayField(models.CharField(max_length=30, null=True, blank=True), null=True)
    post_pic =  models.CharField(max_length=200)

class MyModel(models.Model):
    content = HTMLField()

class ModelFoo(models.Model):
    content = TinyMCEModelField('Foo Content')

# Create your models here.
