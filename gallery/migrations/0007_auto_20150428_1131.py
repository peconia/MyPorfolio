# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20150428_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerygroup',
            name='slug',
            field=models.SlugField(),
        ),
    ]
