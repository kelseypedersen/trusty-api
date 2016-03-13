# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20160313_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segment',
            old_name='overview',
            new_name='overview_id',
        ),
        migrations.AlterField(
            model_name='overview',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', blank=True),
        ),
    ]
