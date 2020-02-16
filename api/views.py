from django.shortcuts import render
from rest_framework import generics, permissions
from shop.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
# Create your views here.

class CategoryAPIView(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated) #jeita permission dibo na seita te eita declare korbo
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryAPINewView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('-id')[:1] #latest category
    serializer_class = CategorySerializer

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAPINewView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-id')[:1] #latest product
    serializer_class = ProductSerializer