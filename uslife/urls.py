from django.conf.urls import patterns, include, url
from uslife.settings import DEVELOPMENT_MODE
import administration
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)

if DEVELOPMENT_MODE:
    urlpatterns = patterns(
        '',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^administration/', include('administration.urls', namespace='administration', app_name='administration')),
    )