from django import forms
from content.models import FeatureGroup, Feature, PermissionGroup


class FeatureGroupForm(forms.ModelForm):
    class Meta:
        model = FeatureGroup
        fields = ['feature_name', 'display_name', 'description_wiki_key', 'description', ]


class FeatureForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = ['feature_group', 'feature_name', 'display_name', 'description_wiki_key', 'description', ]


class PermissionGroupForm(forms.ModelForm):
    class Meta:
        model = PermissionGroup
        fields = ['group_name', 'is_org_admin', 'user_level', ]


class FileUploadForm(forms.Form):
    file_name = forms.CharField(max_length=50)
    file = forms.FileField(label='Please select a file')
    # TODO : specify which form need upload file
