# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20151217_0618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='ch_name',
            new_name='display_name',
        ),
        migrations.RenameField(
            model_name='featuregroup',
            old_name='ch_name',
            new_name='display_name',
        ),
    ]
