# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_ctemplate_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='base_html',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
