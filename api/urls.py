from django.conf.urls import url, patterns, include
from rest_framework import routers
from django.contrib.admin import site
from api.restful import administration_api


urlpatterns = patterns(
    '',
    # url(r'^$', include(site.urls)),
    url(r'customers/$', administration_api.CustomerList.as_view(), name='customer-list'),
)

