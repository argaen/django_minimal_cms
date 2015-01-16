# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_project_base_html'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='base_html',
            new_name='base_template',
        ),
    ]
