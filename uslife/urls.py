from django.conf.urls import patterns, include, url
from uslife.settings import DEVELOPMENT_MODE
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls', namespace='api', app_name='api')),
)

if DEVELOPMENT_MODE:
    urlpatterns = patterns(
        '',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/', include('api.urls', namespace='api', app_name='api')),
    )
