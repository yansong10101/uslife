from django.core.exceptions import ObjectDoesNotExist
from uslife.settings import (AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_DEFAULT_SITE,
                             AWS_BUCKET_ORG_ARCHIVE, AWS_BUCKET_USER_ARCHIVE, AWS_HEADERS, )
from boto.s3.connection import S3Connection
from django.core.files.base import ContentFile
import json


class S3Storage:
    def __init__(self):
        self.connection = S3Connection(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)
        self.bucket = None

    def key_validation(self, key_name):
        pass  # TODO : update validator

    def get_bucket(self, bucket_name):
        self.bucket = self.connection.get_bucket(bucket_name)
        if self.bucket is None:
            raise ObjectDoesNotExist('Bucket : %s Does not exist !' % bucket_name)
        return self.bucket

    def get_default_site_bucket(self):
        return self.get_bucket(AWS_BUCKET_DEFAULT_SITE)

    def get_org_bucket(self):
        return self.get_bucket(AWS_BUCKET_ORG_ARCHIVE)

    def get_user_bucket(self):
        return self.get_bucket(AWS_BUCKET_USER_ARCHIVE)

    def get_all_keys(self):
        return self.bucket.list()

    def get_keys_by_regex(self, regex):
        pass  # TODO : Add regex to filter all target keys

    def upload_file(self, file, key_name):
        new_key = self.bucket.new_key(key_name)
        new_key.set_contents_from_file(file)

    def upload_files(self, file_dict):
        pass  # TODO : upload files with dictionary object. i.e. {'key_name': file, ...}

    def download_file_as_string(self, key_name):
        target_key = self.bucket.get_key(key_name)
        if target_key is not None:
            return target_key.get_contents_as_string()
        return None

    def download_file_as_file(self, key_name):
        file_content = self.download_file_as_string(key_name)
        if file_content is not None:
            return ContentFile(file_content)
        return None

    def delete_file(self, key_name):
        target_key = self.bucket.get_key(key_name)
        if target_key is not None:
            target_key.delete()

    def create_bucket(self, bucket_name):
        # return new created bucket
        return self.connection.create_bucket(bucket_name)
