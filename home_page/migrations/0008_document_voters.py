# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0007_auto_20160419_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='voters',
            field=models.SlugField(default='start_', max_length=200),
        ),
    ]
