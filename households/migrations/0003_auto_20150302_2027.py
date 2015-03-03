# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('households', '0002_auto_20150302_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='fax',
            field=models.CharField(blank=True, null=True, max_length=14),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.CharField(blank=True, null=True, max_length=14),
            preserve_default=True,
        ),
    ]
