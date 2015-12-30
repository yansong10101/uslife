from content.models import FeatureGroup, Feature, Permission, PermissionGroup
from rest_framework import serializers


# Feature Group Model serializers
class FeatureGroupListSerializer(serializers.HyperlinkedModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='api:feature-group-retrieve')

    class Meta:
        model = FeatureGroup
        fields = ('pk', 'detail_url', 'feature_name', )


class FeatureGroupRetrieveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FeatureGroup
        fields = ('pk', 'feature_name', )


# Feature Model serializers
class FeatureListSerializer(serializers.HyperlinkedModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='api:feature-retrieve')
    feature_group = serializers.HyperlinkedRelatedField(view_name='api:feature-group-retrieve', read_only=True)

    class Meta:
        model = Feature
        fields = ('pk', 'detail_url', 'feature_group', 'feature_name', )


class FeatureRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    feature_group = serializers.HyperlinkedRelatedField(view_name='api:feature-group-retrieve', read_only=True)

    class Meta:
        model = Feature
        fields = ('pk', 'feature_group', 'feature_name', )


# Permission serializers
class PermissionListSerializer(serializers.HyperlinkedModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='api:permission-retrieve', read_only=True)
    feature = serializers.HyperlinkedRelatedField(view_name='api:feature-retrieve', read_only=True)

    class Meta:
        model = Permission
        fields = ('pk', 'detail_url', 'feature', 'permission_name', 'permission_type', 'is_active', )


class PermissionRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    feature = serializers.HyperlinkedRelatedField(view_name='api:feature-retrieve', read_only=True)

    class Meta:
        model = Permission
        fields = ('pk', 'feature', 'permission_name', 'permission_type', 'is_active', )


# Permission Group serializers
class PermissionGroupListSerializer(serializers.HyperlinkedModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='api:permission-group-retrieve', read_only=True)
    permission = PermissionRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = PermissionGroup
        fields = ('pk', 'detail_url', 'group_name', 'permission', 'is_org_admin', 'is_super_user', 'is_active', 'user_level', )


class PermissionGroupRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    permission = PermissionRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = PermissionGroup
        fields = ('pk', 'group_name', 'permission', 'is_org_admin', 'is_super_user', 'is_active', 'user_level', )
