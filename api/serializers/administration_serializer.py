from administration.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('pk', 'email', 'first_name', 'last_name', 'created_date', 'last_modified_date', )