
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Func, Value, ExpressionWrapper
from django.http import HttpResponse
from django.db.models.aggregates import Count, Avg, Max, Min
from store.models import Customer, Order, OrderItem, Product
from django.db.models.functions import Concat

# Create your views here.

# def calculate():
#     x = 1
#     y = 2
#     return x


def say_hello(request):
    # x = calculate()
    discounted_price = ExpressionWrapper(
        F('unit_price')*0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(
        discounted_price=discounted_price
    )

    return render(request, 'hello.html', {'name': 'Soumya', 'result': list(queryset)})
    # return HttpResponse('Hello World')
