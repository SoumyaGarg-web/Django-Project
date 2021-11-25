
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Func, Value, ExpressionWrapper
from django.http import HttpResponse
from django.db.models.aggregates import Count, Avg, Max, Min
from store.models import Collection, Customer, Order, OrderItem, Product
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):

    collection = Collection.objects.filter(pk=1).update(featured_product=None)

    return render(request, 'hello.html', {'name': 'Soumya'})
