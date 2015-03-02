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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(null=True, blank=True, max_length=255)),
                ('zip_code', models.CharField(null=True, blank=True, max_length=9)),
                ('phone', models.CharField(null=True, blank=True, max_length=10)),
                ('fax', models.CharField(null=True, blank=True, max_length=10)),
                ('state', models.CharField(null=True, blank=True, choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], max_length=2)),
                ('city', models.CharField(null=True, blank=True, max_length=100)),
                ('website', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
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
        migrations.AddField(
            model_name='person',
            name='schools',
            field=models.ManyToManyField(to='households.School', null=True, related_name='people', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personsubtype',
            name='name',
            field=models.CharField(verbose_name='Subtype', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persontype',
            name='name',
            field=models.CharField(verbose_name='Type', max_length=25),
            preserve_default=True,
        ),
    ]
