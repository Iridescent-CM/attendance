# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('households', '0002_student_attended'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='zip_code',
            field=models.CharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
    ]
