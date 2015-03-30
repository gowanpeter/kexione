# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vv', '0002_auto_20150323_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID'),
            preserve_default=True,
        ),
    ]
