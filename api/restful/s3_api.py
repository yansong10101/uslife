from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django import forms
from content.s3_storage import S3Storage
from uslife.settings import AWS_BUCKET_ORG_WIKI

TEST_S3_KEY_PREFIX = 'test-upload/demo-upload/'


class ImageFileForm(forms.Form):
    file = forms.FileField()


class WikiFileForm(forms.Form):
    old_path = forms.CharField(required=False)
    new_path = forms.CharField()
    page = forms.CharField()


class GetKeysForm(forms.Form):
    key_name = forms.CharField(required=False)
    spec = forms.CharField(required=False)
    suffix = forms.CharField(required=False)
    marker = forms.CharField(required=False)


@api_view(['POST', ])
def upload_image(request):
    # FIXME : update key path and bucket name
    s3 = S3Storage(AWS_BUCKET_ORG_WIKI)
    response_data = {}
    if request.method == 'POST':
        form = ImageFileForm(request.POST, request.FILES)
        if not form.is_valid():
            return Response(data=form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)
        key_prefix = TEST_S3_KEY_PREFIX
        s3_key = s3.upload_image(request.FILES['file'], key_prefix)
        return Response(data={'s3_key': s3_key}, status=status.HTTP_201_CREATED)
    return Response(data=response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST', ])
def upload_wiki(request):
    s3 = S3Storage(AWS_BUCKET_ORG_WIKI)
    response_data = {}
    if request.method == 'POST':
        form = WikiFileForm(request.POST)
        if not form.is_valid():
            return Response(data=form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)
        new_key_name = form.cleaned_data['new_path']
        old_key_name = form.cleaned_data['old_path']
        page = form.cleaned_data['page']
        s3_key = s3.upload_wiki(page, new_key_name, old_key_name)
        return Response(data={'s3_key': s3_key}, status=status.HTTP_201_CREATED)
    return Response(data=response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST', ])
def get_items(request):
    s3 = S3Storage(AWS_BUCKET_ORG_WIKI)
    response_data = {}
    if request.method == 'POST':
        form = GetKeysForm(request.data)
        if form.is_valid():
            key_prefix = form.cleaned_data['key_name'] or ''
            key_spec = form.cleaned_data['spec'] or None
            key_suffix = form.cleaned_data['suffix'] or '/'
            key_marker = form.cleaned_data['marker'] or ''
            response_data['result_list'] = s3.get_sub_keys_with_spec(key_prefix, key_spec, key_suffix, key_marker)
            return Response(data=response_data, status=status.HTTP_200_OK)
        return Response(data=form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)
    return Response(data=response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
