from rest_framework import serializers
from customer.models import Customer
from vendor.models import Vendor

class CustomerSerializer(serializers.ModelSerializer):
    # Serialises and deserialises
    class Meta:
        model = Customer
        fields = '__all__'