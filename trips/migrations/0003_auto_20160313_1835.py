# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20160313_1805'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Segments',
            new_name='Segment',
        ),
    ]
