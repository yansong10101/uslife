from administration.models import Customer, University, OrgAdmin, CustomerUPG
from rest_framework import serializers


# University Model serializer
class UniversityListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:university-retrieve')

    class Meta:
        model = University
        fields = ('url', 'university_name', 'university_code', )


class UniversityRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = ('pk', 'university_name', 'university_code', )


# Org Admin serializer
class OrgAdminListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrgAdmin
        fields = ('university', 'username', 'email', 'last_modified_date', 'last_login_date', )


class OrgAdminRetrieveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrgAdmin
        fields = ('university', 'username', 'email', 'last_modified_date', 'last_login_date', )


# Customer Model serializer
class CustomerListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:customer-retrieve')

    class Meta:
        model = Customer
        fields = ('url', 'email', 'first_name', 'last_name', 'created_date', 'last_modified_date', )


class CustomerRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'email', 'first_name', 'last_name', 'created_date', 'last_modified_date', )


# Customer University Permission Group serializer
class CustomerUPGListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomerUPG
        fields = ('customer', 'university', 'permission_group', 'grant_level', )


class CustomerUPGRetrieveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomerUPG
        fields = ('customer', 'university', 'permission_group', 'grant_level', )
