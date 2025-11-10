from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import Product , Category , Review, ProductImage
from .serializers import ProductSerializer,CategorySerializer, ReviewSerializer, ProductImageSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser, AllowAny
from .paginitions import DefaultPaginition
from api.permissions import IsAdminReadOnly 
from product.permissions import IsReviewAuthorOrReadonly
from drf_yasg.utils import swagger_auto_schema


#Product Part
class ProductViewSet(ModelViewSet):
    """
    API end-point for managing products in the e-commerce store
    - Allow Authenticated Admin to create, update, and delete products
    - Allows Users to browse and filter
    - Support searching by name, description, and category 
    - Support ordering by price and updated_at
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends =[DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_class = ProductFilter
    pagination_class = DefaultPaginition
    search_fields = ['name','description','category__name']
    ordering_fields = ['price', 'created_at'] 
    permission_classes = [IsAdminReadOnly]

    def get_queryset(self):
        return Product.objects.prefetch_related('images').all()
    @swagger_auto_schema(
            operation_summary='Retrive a list of products'
    )
    def list(self, request, *args, **kwargs):
        """ Retrive all the products """
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
            operation_summary = 'Create a Product By admin',
            operation_description='This allow an admin to create a product',
            request_body=ProductSerializer,
            responses={
                201: ProductSerializer,
                400: 'Bad Request'
            }
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create product"""
        return super().create(request, *args, **kwargs)




class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminReadOnly]
    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs.get('product_pk'))
    def perform_create(self, serializer):
        return serializer.save(product_id = self.kwargs.get('product_pk'))
    

#Category Part
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(
            product_count = Count('products')).all()
    serializer_class=CategorySerializer
    permission_classes = [IsAdminReadOnly]


#Review Part
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadonly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        review = Review.objects.filter(product_id = self.kwargs.get('product_pk'))
        return review
    def get_serializer_context(self):
        return {'product_id': self.kwargs.get('product_pk')}
    
