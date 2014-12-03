# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blogName', models.CharField(max_length=50)),
                ('contactInfo', models.CharField(max_length=500)),
                ('owner', models.CharField(max_length=50)),
                ('intro', models.CharField(max_length=1000)),
                ('picture', models.CharField(max_length=150)),
                ('visitor', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
