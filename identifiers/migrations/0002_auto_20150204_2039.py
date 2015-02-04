# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identifiers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keytag',
            name='holder',
            field=models.ForeignKey(blank=True, null=True, to='households.Student', related_name='keytags'),
            preserve_default=True,
        ),
    ]
