
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
from django.db import transaction


def say_hello(request):

    with transaction.atomic():  # returns context manager
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()

    return render(request, 'hello.html', {'name': 'Soumya'})
