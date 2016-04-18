# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0008_auto_20160418_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
