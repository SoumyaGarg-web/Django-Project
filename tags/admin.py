from django.contrib import admin

from store import models
from .models import Tag
# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']
