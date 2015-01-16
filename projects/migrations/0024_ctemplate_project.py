# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20150116_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctemplate',
            name='project',
            field=models.ManyToManyField(to='projects.Project', verbose_name='Project'),
            preserve_default=True,
        ),
    ]
