# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20150112_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='researcher',
            old_name='photo',
            new_name='image',
        ),
    ]
