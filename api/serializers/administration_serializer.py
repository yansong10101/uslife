from administration.models import Customer, University
from content.models import FeatureGroup
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
        fields = ('url', 'university', 'email', 'first_name', 'last_name', 'created_date', 'last_modified_date', )


class CustomerRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'university', 'email', 'first_name', 'last_name', 'created_date', 'last_modified_date', )


class FeatureGroupListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:feature-group-retrieve')

    class Meta:
        model = FeatureGroup
        fields = ('url', 'pk', 'feature_name', 'display_name', )


class FeatureGroupRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeatureGroup
        fields = ('pk', 'feature_name', 'display_name', )
