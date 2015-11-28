from administration.models import Customer, University
from rest_framework import serializers


class UniversityListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:university-retrieve')

    class Meta:
        model = University
        fields = ('url', 'university_name', 'university_code', )


class UniversityRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = ('pk', 'university_name', 'university_code', )


class CustomerListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:customer-retrieve')

    class Meta:
        model = Customer
        fields = ('url', 'email', 'first_name', 'last_name', 'created_date', 'last_modified_date', )


class CustomerRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'email', 'first_name', 'last_name', 'created_date', 'last_modified_date', )
