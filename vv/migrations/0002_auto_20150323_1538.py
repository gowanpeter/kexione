# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Logo_name', models.CharField(blank=True, max_length=8)),
                ('logo_description', models.CharField(blank=True, max_length=12)),
                ('stamp_name', models.CharField(blank=True, max_length=8)),
                ('picture', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='logo_link_piece',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('feature', models.CharField(default='too true', max_length=12)),
                ('Logo', models.ForeignKey(to='vv.Logo')),
                ('Piece', models.ForeignKey(to='vv.Piece')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='logo',
            name='logo_pieces',
            field=models.ManyToManyField(through='vv.logo_link_piece', to='vv.Piece'),
            preserve_default=True,
        ),
    ]
