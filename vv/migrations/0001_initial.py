# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(blank=True, max_length=8)),
                ('condition', models.CharField(default='b', choices=[('a', 'Pristine'), ('b', 'Used, good'), ('c', 'Used, worn'), ('d', 'Cracked / chipped'), ('e', 'Broken')], max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('documentation_name', models.CharField(blank=True, max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='documentation_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('documentation_date', models.DateField(blank=True, null=True)),
                ('documentation_author', models.CharField(blank=True, max_length=8)),
                ('documentation_media', models.CharField(blank=True, max_length=8)),
                ('documentation_location', models.CharField(blank=True, max_length=8)),
                ('documentation', models.ForeignKey(to='vv.Documentation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='exhibition_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExhibitionLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('exhibition_name', models.CharField(blank=True, max_length=8)),
                ('exhibition_date', models.DateField(blank=True, null=True)),
                ('exhibition_description', models.CharField(blank=True, max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='glaze_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('batch', models.CharField(default='200', max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GlazeLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('glaze_name', models.CharField(default='boola', unique=True, max_length=8)),
                ('glaze_description', models.CharField(blank=True, max_length=12)),
                ('glaze_begin_date', models.DateField(blank=True, null=True)),
                ('glaze_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='heath_line_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('feature', models.CharField(default='too true', max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HeathLineLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('heath_line_name', models.CharField(blank=True, max_length=8)),
                ('heath_line_begin_date', models.DateField(blank=True, null=True)),
                ('heath_line_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='maker_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('feature', models.CharField(default='too true', max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MakerLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('maker_name', models.CharField(blank=True, max_length=8)),
                ('maker_location', models.CharField(blank=True, max_length=8)),
                ('maker_start_date', models.DateField(blank=True, null=True)),
                ('maker_stop_date', models.DateField(blank=True, null=True)),
                ('maker_description', models.CharField(blank=True, max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='material_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('feature', models.CharField(default='too true', max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaterialLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('material_name', models.CharField(blank=True, max_length=8)),
                ('material_description', models.CharField(blank=True, max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='method_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('feature', models.CharField(default='too true', max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('method_name', models.CharField(blank=True, max_length=8)),
                ('method_description', models.CharField(blank=True, max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('catalogue_id', models.CharField(max_length=8)),
                ('heath_id', models.CharField(blank=True, max_length=8)),
                ('piece_name', models.CharField(blank=True, max_length=6)),
                ('piece_description', models.CharField(blank=True, max_length=12)),
                ('manufactured_date', models.DateField(blank=True, null=True)),
                ('length_inches', models.IntegerField(blank=True, null=True)),
                ('width_inches', models.IntegerField(blank=True, null=True)),
                ('height_inches', models.IntegerField(blank=True, null=True)),
                ('weight_ounces', models.IntegerField(blank=True, null=True)),
                ('length_mm', models.IntegerField(blank=True, null=True)),
                ('width_mm', models.IntegerField(blank=True, null=True)),
                ('height_mm', models.IntegerField(blank=True, null=True)),
                ('weight_grams', models.IntegerField(blank=True, null=True)),
                ('cataloguer', models.CharField(blank=True, max_length=8)),
                ('catalogue_date', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='publication_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=8)),
                ('publication_author', models.CharField(blank=True, max_length=8)),
                ('piece', models.ForeignKey(to='vv.Piece')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicationLookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('publication_name', models.CharField(blank=True, max_length=8)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('publication_author', models.CharField(blank=True, max_length=8)),
                ('publication_media', models.CharField(blank=True, max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SetCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('set_collection_name', models.CharField(blank=True, max_length=8)),
                ('setcollection_location', models.CharField(blank=True, max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='setCollection_link_piece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=12)),
                ('Piece', models.ForeignKey(to='vv.Piece')),
                ('SetCollection', models.ForeignKey(to='vv.SetCollection')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='setcollection',
            name='set_collection_piece',
            field=models.ManyToManyField(through='vv.setCollection_link_piece', to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication_link_piece',
            name='publication',
            field=models.ForeignKey(to='vv.PublicationLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='methodlookup',
            name='method_pieces',
            field=models.ManyToManyField(through='vv.method_link_piece', to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='method_link_piece',
            name='MethodLookup',
            field=models.ForeignKey(to='vv.MethodLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='method_link_piece',
            name='Piece',
            field=models.ForeignKey(to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='materiallookup',
            name='material_pieces',
            field=models.ManyToManyField(through='vv.material_link_piece', to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='material_link_piece',
            name='MaterialLookup',
            field=models.ForeignKey(to='vv.MaterialLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='material_link_piece',
            name='Piece',
            field=models.ForeignKey(to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='makerlookup',
            name='maker_pieces',
            field=models.ManyToManyField(through='vv.maker_link_piece', to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maker_link_piece',
            name='MakerLookup',
            field=models.ForeignKey(to='vv.MakerLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maker_link_piece',
            name='Piece',
            field=models.ForeignKey(to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='heathlinelookup',
            name='heath_line_pieces',
            field=models.ManyToManyField(through='vv.heath_line_link_piece', to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='heath_line_link_piece',
            name='heath_line',
            field=models.ForeignKey(to='vv.HeathLineLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='heath_line_link_piece',
            name='piece',
            field=models.ForeignKey(to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glazelookup',
            name='glaze_pieces',
            field=models.ManyToManyField(through='vv.glaze_link_piece', to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glaze_link_piece',
            name='glaze',
            field=models.ForeignKey(to='vv.GlazeLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glaze_link_piece',
            name='piece',
            field=models.ForeignKey(to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exhibition_link_piece',
            name='exhibition',
            field=models.ForeignKey(to='vv.ExhibitionLookup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exhibition_link_piece',
            name='piece',
            field=models.ForeignKey(to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentation_link_piece',
            name='piece',
            field=models.ForeignKey(to='vv.Piece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentation',
            name='documentation_pieces',
            field=models.ManyToManyField(through='vv.documentation_link_piece', to='vv.Piece'),
            preserve_default=True,
        ),
    ]
