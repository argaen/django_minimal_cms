# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_auto_20150116_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionorder',
            name='on_menu',
            field=models.BooleanField(default=b'True', help_text='Create a menu item in the navigation bar for this section', verbose_name='On menu'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sectionorder',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sectionorder',
            name='project',
            field=models.ForeignKey(verbose_name='Project', to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sectionorder',
            name='section',
            field=models.ForeignKey(verbose_name='Section', to='projects.Section'),
            preserve_default=True,
        ),
    ]
