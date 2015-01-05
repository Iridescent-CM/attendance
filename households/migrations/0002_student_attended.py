# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
        ('households', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='attended',
            field=models.ManyToManyField(related_name='attendees', to='programs.Session'),
            preserve_default=True,
        ),
    ]
