from api.serializers.administration_serializer import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.response import Response


class UniversityList(generics.ListCreateAPIView):
    queryset = University.universities
    serializer_class = UniversityListSerializer
    paginate_by = 15


class UniversityRetrieve(generics.RetrieveUpdateAPIView):
    queryset = University.universities
    serializer_class = UniversityRetrieveSerializer


class CustomerList(generics.ListAPIView):
    queryset = Customer.customers
    serializer_class = CustomerListSerializer
    paginate_by = 15


class CustomerRetrieve(generics.RetrieveAPIView):
    queryset = Customer.customers
    serializer_class = CustomerRetrieveSerializer
