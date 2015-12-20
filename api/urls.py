from django.conf.urls import url, patterns, include
from rest_framework import routers
from api.restful import administration_api, content_api


urlpatterns = patterns(
    '',
    url(r'universities/$', administration_api.UniversityList.as_view(), name='university-list'),
    url(r'universities/(?P<pk>[0-9])+/$', administration_api.UniversityRetrieve.as_view(), name='university-retrieve'),
    url(r'customers/$', administration_api.CustomerList.as_view(), name='customer-list'),
    url(r'customers/(?P<pk>[0-9]+)/$', administration_api.CustomerRetrieve.as_view(), name='customer-retrieve'),
    url(r'feature-groups/$', content_api.FeatureGroupList.as_view(), name='feature-group-list'),
    url(r'feature-groups/(?P<pk>[0-9]+)/$', content_api.FeatureGroupDetail.as_view(), name='feature-group-retrieve'),
)
