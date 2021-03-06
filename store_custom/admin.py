from django.contrib import admin
from store.admin import ProductAdmin
from tags.models import TaggedItem
from store.models import Product
from django.contrib.contenttypes.admin import GenericTabularInline


# Register your models here.

class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']
    extra = 0


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
