# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('households', '0003_auto_20150302_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='zip_code',
            field=models.CharField(null=True, max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
