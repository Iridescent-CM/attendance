# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('households', '0005_auto_20150205_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cell_phone',
            field=models.CharField(max_length=25, blank=True, null=True),
            preserve_default=True,
        ),
    ]
