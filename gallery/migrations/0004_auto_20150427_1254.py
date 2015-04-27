# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20150427_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, default='')),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='group',
            field=models.ForeignKey(to='gallery.GalleryGroup'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
