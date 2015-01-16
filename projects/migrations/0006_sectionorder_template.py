# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_researcher_institution'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionorder',
            name='template',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
