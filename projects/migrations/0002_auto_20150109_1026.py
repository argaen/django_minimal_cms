# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sectionorder',
            options={'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
    ]
