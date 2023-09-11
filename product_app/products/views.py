from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

# class ProductList(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         queryset = Product.objects.all()
#         keyword = self.request.query_params.get('keyword')
#         if keyword is not None:
#             queryset = queryset.filter(name=keyword)
#         return queryset

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = '__all__'



class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer