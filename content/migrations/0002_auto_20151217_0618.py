# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=150)),
                ('ch_name', models.CharField(blank=True, max_length=150)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='featuregroup',
            name='ch_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='featuregroup',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='featuregroup',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='feature_group',
            field=models.ForeignKey(related_name='sub_feature_feature_group', to='content.FeatureGroup'),
        ),
    ]
