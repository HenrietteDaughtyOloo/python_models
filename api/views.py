from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status # Import status to handle HTTP status codes
# Create your views here.
from customer.models import Customer
from .serializers import CustomerSerializer

class CustomerListViews(APIView):
    def get(self,request):
        customers= Customer.objects.all()
        # Serializes the querryset using customer sterializer
        serializer = CustomerSerializer(customers, many = True)
        # Bring back serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        # creating a new instance in the customer serializer and populate it with data
        serializer = CustomerSerializer(data = request.data)

        #check if data provided is Valid acccording to the Serializer rules
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CustomerDetailView(APIView):
    def get_object(self, id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            raise Http404
    def get (self, request, pk, format=None):
        Customer=self.get_object(pk)
        serializer=CustomerSerializer(Customer)
        return Response(serializer.data)
    def put(self, request, pk, format= None):
        customer = self.get_object(id=id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=statys.HTTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)