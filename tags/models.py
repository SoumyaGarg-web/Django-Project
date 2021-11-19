from typing import Generic
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # what tag applied to what object.
    # Type(Product, Video, Article)
    # ID
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # table in which object can be found
    object_id = models.PositiveIntegerField() # primary key id for that object
    content_object =  GenericForeignKey() #read actual object for which particular tag is applied to