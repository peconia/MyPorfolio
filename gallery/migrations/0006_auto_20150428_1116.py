# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_gallerygroup_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerygroup',
            name='slug',
            field=models.SlugField(),
        ),
    ]
