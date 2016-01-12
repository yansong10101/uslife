from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django import forms
from content.s3_storage import S3Storage

TEST_S3_BUCKET = 'test-2016'
TEST_S3_KEY_PREFIX = 'test-upload/demo-upload/'


class ImageFileForm(forms.Form):
    file = forms.FileField()


class WikiFileForm(forms.Form):
    old_path = forms.CharField(required=False)
    new_path = forms.CharField()
    page = forms.CharField()


@api_view(['POST', ])
def upload_image(request):
    # FIXME : update key path and bucket name
    s3 = S3Storage(TEST_S3_BUCKET)
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
    s3 = S3Storage(TEST_S3_BUCKET)
    response_data = {}
    if request.method == 'POST':
        form = WikiFileForm(request.POST)
        if not form.is_valid():
            return Response(data=form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)
        new_key_name = form.cleaned_data['old_path']
        old_key_name = form.cleaned_data['new_path']
        page = form.cleaned_data['page']
        s3_key = s3.upload_wiki(page, new_key_name, old_key_name)
        return Response(data={'s3_key': s3_key}, status=status.HTTP_201_CREATED)
    return Response(data=response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
