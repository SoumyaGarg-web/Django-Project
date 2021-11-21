
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Func, Value, ExpressionWrapper
from django.http import HttpResponse
from django.db.models.aggregates import Count, Avg, Max, Min
from store.models import Customer, Order, OrderItem, Product
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product)

    queryset = TaggedItem.objects.select_related('tag').filter(
        content_type=content_type,
        object_id=1
    )

    return render(request, 'hello.html', {'name': 'Soumya', 'result': list(queryset)})
    # return HttpResponse('Hello World')
