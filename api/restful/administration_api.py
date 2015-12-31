from api.serializers.administration_serializer import *
from administration.forms import UniversityForm, OrgAdminCreateForm, CustomerCreationForm, CustomerUPGForm
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# University APIs
class UniversityList(generics.ListAPIView):
    queryset = University.universities
    serializer_class = UniversityListSerializer
    paginate_by = 15


class UniversityRetrieve(generics.RetrieveAPIView):
    queryset = University.universities
    serializer_class = UniversityRetrieveSerializer


@api_view(['POST', 'PUT', ])
def create_update_university(request, pk=None):
    response_data = {}
    if request.method == 'POST' or request.method == 'PUT':
        if pk is None:
            form = UniversityForm(request.POST)
            if not form.is_valid():
                return Response(data=form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)
            University.universities.create_university(**form.cleaned_data)
        else:
            university = get_object_or_404(University, pk=pk)
            form = UniversityForm(request.POST, instance=university)
            if not form.is_valid():
                return Response(data=form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)
            form.save()
        return Response(data=response_data, status=status.HTTP_201_CREATED)
    return Response(data=response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Org Admin APIs
class OrgAdminList(generics.ListAPIView):
    queryset = OrgAdmin.org_admins
    serializer_class = OrgAdminListSerializer
    paginate_by = 15


class OrgAdminRetrieve(generics.RetrieveAPIView):
    queryset = OrgAdmin.org_admins
    serializer_class = OrgAdminRetrieveSerializer


@api_view(['POST', ])
def create_org_admin(request):
    response_data = {}
    if request.method == 'POST':
        form = OrgAdminCreateForm(request.POST)
        if not form.is_valid():
            return Response(data=form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)
        form.clean_password2()
        form.save()
        return Response(data=response_data, status=status.HTTP_201_CREATED)
    return Response(data=response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Customer APIs
class CustomerList(generics.ListAPIView):
    queryset = Customer.customers
    serializer_class = CustomerListSerializer
    paginate_by = 15


class CustomerRetrieve(generics.RetrieveAPIView):
    queryset = Customer.customers
    serializer_class = CustomerRetrieveSerializer


@api_view(['POST', ])
def create_customer(request):
    response_data = {}
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if not form.is_valid():
            return Response(data=form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)
        form.clean_password2()
        form.save()
        return Response(data=response_data, status=status.HTTP_201_CREATED)
    return Response(data=response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# CustomerUPG APIs
class CustomerUPGList(generics.ListAPIView):
    queryset = CustomerUPG.customer_upg
    serializer_class = CustomerUPGListSerializer
    paginate_by = 15


class CustomerUPGRetrieve(generics.RetrieveAPIView):
    queryset = CustomerUPG.customer_upg
    serializer_class = CustomerUPGRetrieveSerializer


@api_view(['POST', ])
def create_customer_upg(request):
    response_data = {}
    if request.method == 'POST':
        form = CustomerUPGForm(request.POST)
        if not form.is_valid() or form.validate_existing():
            return Response(data=form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)
        CustomerUPG.customer_upg.create_customer_upg(**form.cleaned_data)
        return Response(data=response_data, status=status.HTTP_201_CREATED)
    return Response(data=response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
