from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Collection, Product
from .serializers import ProductSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from store import serializers
# Create your views here.


@api_view()
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    serializer = serializers.ProductSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)


@api_view()
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def collection_details(request, pk):
    queryset = Collection.objects.all()
    serializer = serializers.CollectionSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)
