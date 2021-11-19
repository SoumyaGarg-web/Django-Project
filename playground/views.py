from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.http import HttpResponse
from django.db.models.aggregates import Count, Avg, Max, Min
from store.models import Customer, Order, OrderItem, Product
from django.db.models import Value

# Create your views here.

# def calculate():
#     x = 1
#     y = 2
#     return x


def say_hello(request):
    # x = calculate()
    queryset = Customer.objects.annotate(is_new=Value(True))

    return render(request, 'hello.html', {'name': 'Soumya', 'result': list(queryset)})
    # return HttpResponse('Hello World')
