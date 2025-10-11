#class ProductSerializer(serializers.Serializer):
#   id=serializers.IntegerField()
#   name=serializers.CharField()
#   price=serializers.DecimalField(max_digits=10 , decimal_places=2)
#   price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
#category=serializers.PrimaryKeyRelatedField(
#  queryset = Category.objects.all()
#   )
    #category=CategorySerializer()
    #category=serializers.HyperlinkedRelatedField(
#      queryset=Category.objects.all(),
#      view_name='view_spesific_category'
#    )

#    def calculate_tax(self, product):
#       return round(product.price * Decimal(1.1) , 2)

from rest_framework import serializers
from product.models import Category,Product
from decimal import Decimal
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description', 'product_count']
    product_count = serializers.IntegerField( read_only = True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','price','stock','category','price_with_tax']  # new Field added name 'other'
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    #category = serializers.HyperlinkedRelatedField(
    #  queryset = Category.objects.all(),
     # view_name = 'view_spesific_category',
    # )
    def calculate_tax(self,product):
        return round(product.price * Decimal(1.1))
    
    def validate_price(self, price):
        if price < 0 :
            raise serializers.ValidationError("Price not Allowed Negative Number")
        return price
    
    #def create(self, validated_data):
    #    product = Product(**validated_data)
    #    product.other = 1            # new Field adde in Product Model(DB)
    #    product.save()
    #    return product       
              
