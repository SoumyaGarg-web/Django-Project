from typing import Generic
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)

        queryset = TaggedItem.objects.select_related('tag').filter(
            content_type=content_type,
            object_id=obj_id
        )

        return queryset


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag applied to what object.
    # Type(Product, Video, Article)
    # ID
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # table in which object can be found
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()  # primary key id for that object
    # read actual object for which particular tag is applied to
    content_object = GenericForeignKey()
