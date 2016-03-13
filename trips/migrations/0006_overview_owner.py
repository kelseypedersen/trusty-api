# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0005_auto_20160313_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='overview',
            name='owner',
            field=models.ForeignKey(related_name='overviews', default='0', to=settings.AUTH_USER_MODEL),
        ),
    ]
