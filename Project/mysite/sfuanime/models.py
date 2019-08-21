from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from django.utils import timezone




class Posts(models.Model):

    post_title  = models.CharField(max_length=200)
    post_content  = models.CharField(max_length=200)
    post_date = models.DateTimeField()


# Create your models here.
