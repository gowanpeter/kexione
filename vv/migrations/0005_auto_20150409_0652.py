# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vv', '0004_auto_20150328_0815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='condition',
            options={'verbose_name_plural': 'conditions', 'verbose_name': 'condition'},
        ),
        migrations.AlterModelOptions(
            name='documentation',
            options={'verbose_name_plural': 'documentation', 'verbose_name': 'documentation'},
        ),
        migrations.AlterModelOptions(
            name='documentation_link_piece',
            options={'verbose_name_plural': 'documentation pieces', 'verbose_name': 'documentation link'},
        ),
        migrations.AlterModelOptions(
            name='exhibition_link_piece',
            options={'verbose_name_plural': 'exhibition pieces', 'verbose_name': 'exhibition link'},
        ),
        migrations.AlterModelOptions(
            name='exhibitionlookup',
            options={'verbose_name_plural': 'exhibitions', 'verbose_name': 'exhibition'},
        ),
        migrations.AlterModelOptions(
            name='glaze_link_piece',
            options={'verbose_name_plural': 'glaze pieces', 'verbose_name': 'glaze link'},
        ),
        migrations.AlterModelOptions(
            name='glazelookup',
            options={'verbose_name_plural': 'glazes', 'verbose_name': 'glaze'},
        ),
        migrations.AlterModelOptions(
            name='heath_line_link_piece',
            options={'verbose_name_plural': 'heath line pieces', 'verbose_name': 'heath line link'},
        ),
        migrations.AlterModelOptions(
            name='heathlinelookup',
            options={'verbose_name_plural': 'heath lines', 'verbose_name': 'heath line '},
        ),
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name_plural': 'logos', 'verbose_name': 'logo'},
        ),
        migrations.AlterModelOptions(
            name='maker_link_piece',
            options={'verbose_name_plural': 'maker pieces', 'verbose_name': 'maker link'},
        ),
        migrations.AlterModelOptions(
            name='makerlookup',
            options={'verbose_name_plural': 'makers', 'verbose_name': 'maker'},
        ),
        migrations.AlterModelOptions(
            name='material_link_piece',
            options={'verbose_name_plural': 'material pieces', 'verbose_name': 'material link'},
        ),
        migrations.AlterModelOptions(
            name='materiallookup',
            options={'verbose_name_plural': 'materials', 'verbose_name': 'material'},
        ),
        migrations.AlterModelOptions(
            name='method_link_piece',
            options={'verbose_name_plural': 'method pieces', 'verbose_name': 'method link'},
        ),
        migrations.AlterModelOptions(
            name='methodlookup',
            options={'verbose_name_plural': 'methods', 'verbose_name': 'method'},
        ),
        migrations.AlterModelOptions(
            name='piece',
            options={'verbose_name_plural': 'pieces', 'verbose_name': 'piece'},
        ),
        migrations.AlterModelOptions(
            name='publication_link_piece',
            options={'verbose_name_plural': 'publication pieces', 'verbose_name': 'publication link'},
        ),
        migrations.AlterModelOptions(
            name='publicationlookup',
            options={'verbose_name_plural': 'publications', 'verbose_name': 'publication'},
        ),
        migrations.AlterModelOptions(
            name='setcollection',
            options={'verbose_name_plural': 'collections', 'verbose_name': 'collection'},
        ),
        migrations.AlterModelOptions(
            name='setcollection_link_piece',
            options={'verbose_name_plural': 'collection pieces', 'verbose_name': 'collection link'},
        ),
        migrations.AddField(
            model_name='piece',
            name='post_edith',
            field=models.NullBooleanField(),
        ),
    ]
