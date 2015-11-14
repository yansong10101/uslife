# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lifeuserprofile',
            old_name='first_name',
            new_name='first_username',
        ),
        migrations.RenameField(
            model_name='lifeuserprofile',
            old_name='last_name',
            new_name='last_username',
        ),
    ]
