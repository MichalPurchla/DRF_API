from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from rest_framework import generics
# def api_home(request, *args, **kwargs):
#     body = request.body
#     print(type(body))
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
#     print(request.headers)
#     print(request.content_type)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     data['params'] = dict(request.GET)
#     print(data)
#     print(request.GET) #-> URL query parameters
#     print(request.POST) #-> URL parameters
#     return JsonResponse(data)
# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by('?').first()
#     data = {}
#     if instance:
#         # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)


