# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('households', '0004_auto_20150204_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=9)),
                ('phone', models.CharField(max_length=10)),
                ('state', models.CharField(blank=True, choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], null=True, max_length=2)),
                ('city', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParentGuardian',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, null=True, max_length=50)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null=True, max_length=2)),
                ('email', models.EmailField(blank=True, null=True, max_length=75)),
                ('cell_phone', models.CharField(blank=True, null=True, max_length=25)),
                ('work_phone', models.CharField(blank=True, null=True, max_length=25)),
                ('other_phone', models.CharField(blank=True, null=True, max_length=25)),
                ('relation', models.CharField(blank=True, choices=[('P', 'Parent'), ('S', 'Sibling'), ('G', 'Grandparent'), ('O', 'Other')], null=True, max_length=1)),
                ('household', models.ForeignKey(to='households.Household', related_name='parentguardians', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Parent/Guardian',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='student',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='student',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='cell_phone',
            field=models.CharField(blank=True, null=True, max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, null=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='household',
            field=models.ForeignKey(to='households.Household', related_name='students', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null=True, max_length=2),
            preserve_default=True,
        ),
    ]
