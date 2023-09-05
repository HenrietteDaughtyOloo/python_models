from rest_framework.views import APIView
from rest_framework. response import Response
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
    # def post(self, request):
    #     # creating a new instance in the customer serializer and populate it with data
    #     serializer = CustomerSerializer(data = request.data)

    #     #check if data provided is Valid acccording to the Serializer rules
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, )
    #     #
    
