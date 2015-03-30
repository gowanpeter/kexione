# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vv', '0003_auto_20150327_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='glaze_link_piece',
            old_name='glaze',
            new_name='glazeLookup',
        ),
    ]
