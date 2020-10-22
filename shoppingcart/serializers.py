from rest_framework import serializers 
from shoppingcart.models import Products
 
 
class ProductsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Products
        fields = ('id',
                  'title',
                  'description',
                  'published')