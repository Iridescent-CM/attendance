# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('households', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('global_id_type', models.CharField(max_length=10)),
                ('global_id_value', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255, blank=True, null=True)),
                ('zip_code', models.CharField(max_length=9, blank=True, null=True)),
                ('phone', models.CharField(max_length=10, blank=True, null=True)),
                ('fax', models.CharField(max_length=10, blank=True, null=True)),
                ('state', models.CharField(max_length=2, choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], blank=True, null=True)),
                ('city', models.CharField(max_length=100, blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='school',
            unique_together=set([('global_id_type', 'global_id_value')]),
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AlterModelOptions(
            name='personsubtype',
            options={'verbose_name': 'Subtype'},
        ),
        migrations.AlterModelOptions(
            name='persontype',
            options={'verbose_name': 'Type'},
        ),
        migrations.AlterField(
            model_name='personsubtype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Subtype'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persontype',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Type'),
            preserve_default=True,
        ),
    ]
