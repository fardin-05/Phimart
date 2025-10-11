from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Product , Category
from .serializers import ProductSerializer,CategorySerializer
from django.db.models import Count
#Product Part
class ViewProduct(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many = True, )
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
class ViewSpecificProduct(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product , pk = id)
        serializer = ProductSerializer( product )
        return Response(serializer.data)
    def put(self, request, id):
        product = get_object_or_404(Product , pk = id)
        serializer = ProductSerializer(product , data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        product = get_object_or_404(Product, pk = id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Category Part
class ViewCategory(APIView):
    def get(self , request):
        category = Category.objects.annotate(
            product_count = Count('products')).all()
        serializer = CategorySerializer(category, many = True)
        return Response(serializer.data)
    def post(self , request):
        serializer = CategorySerializer (data = request.data)
        serializer.is_valid( raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
class ViewSpecificCategory(APIView):
    def get(self,request,pk):
        category = get_object_or_404 (Category.objects.annotate (product_count = Count('products')) , pk = pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    def put(self,request,pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk = pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
