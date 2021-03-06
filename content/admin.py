from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from content.forms import *


class FeatureGroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'feature_name', )
    ordering = ('feature_name', )


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'feature_group', 'feature_name', )
    ordering = ('feature_name', )

admin.site.register(FeatureGroup, FeatureGroupAdmin)
# We want to use API to create feature, it will auto generate corresponding permissions
# admin.site.register(Feature, FeatureAdmin)
