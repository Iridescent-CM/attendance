# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
