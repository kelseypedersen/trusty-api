# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_auto_20160313_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overview',
            name='owner',
            field=models.ForeignKey(related_name='overviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
