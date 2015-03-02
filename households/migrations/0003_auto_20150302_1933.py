# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('households', '0002_auto_20150302_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='schools',
            field=models.ManyToManyField(related_name='people', null=True, blank=True, to='households.School'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='global_id_type',
            field=models.CharField(max_length=10, verbose_name='Type of GID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='global_id_value',
            field=models.CharField(max_length=10, verbose_name='GID'),
            preserve_default=True,
        ),
    ]
