# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20160313_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='overview',
            name='activity_type',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='overview',
            name='length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='overview',
            name='season',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='segment',
            name='country',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='segment',
            name='province',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='segment',
            name='region',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='overview',
            name='title',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
