# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('households', '0003_student_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='attended',
            field=models.ManyToManyField(null=True, blank=True, to='programs.Session', related_name='attendees'),
            preserve_default=True,
        ),
    ]
