# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_project_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='times_cited',
        ),
    ]
