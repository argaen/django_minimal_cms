# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20150116_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Template',
                'verbose_name_plural': 'Templates',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='sectionorder',
            name='content',
        ),
        migrations.AlterField(
            model_name='sectionorder',
            name='template',
            field=models.ForeignKey(default=1, verbose_name='Template', to='projects.CTemplate'),
            preserve_default=False,
        ),
    ]
