from rest_framework import serializers
from customer.models import Customer
from vendor.models import Vendor
from my_cart.models import MyCart
from inventory.models import Product

class CustomerSerializer(serializers.ModelSerializer):
    # Serialises and deserialises
    class Meta:
        model = Customer
        fields = '__all__'
       
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class MyCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCart
        fields ='__all__'
