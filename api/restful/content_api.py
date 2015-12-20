from api.serializers.administration_serializer import *
from rest_framework import generics

class FeatureGroupList(generics.ListCreateAPIView):
    queryset = FeatureGroup.feature_groups
    serializer_class = FeatureGroupListSerializer
    paginate_by = 15


class FeatureGroupDetail(generics.RetrieveUpdateAPIView):
    queryset = FeatureGroup.feature_groups
    serializer_class = FeatureGroupRetrieveSerializer
