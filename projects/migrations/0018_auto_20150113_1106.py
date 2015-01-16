# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20150113_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('project', models.ManyToManyField(to='projects.Project', verbose_name='Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='article',
            name='id',
        ),
        migrations.RemoveField(
            model_name='article',
            name='project',
        ),
        migrations.RemoveField(
            model_name='article',
            name='published',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='id',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='project',
        ),
        migrations.RemoveField(
            model_name='researcher',
            name='published',
        ),
        migrations.AddField(
            model_name='article',
            name='genericobject_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='projects.GenericObject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researcher',
            name='genericobject_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='projects.GenericObject'),
            preserve_default=False,
        ),
    ]
