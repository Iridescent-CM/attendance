# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('households', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keytag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('barcode', models.CharField(max_length=20)),
                ('holder', models.ForeignKey(null=True, related_name='keytags', blank=True, to='households.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
