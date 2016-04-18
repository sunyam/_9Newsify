# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0007_auto_20160418_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='likes',
        ),
        migrations.AddField(
            model_name='document',
            name='rating_dislikes',
            field=models.PositiveIntegerField(default=0, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='rating_likes',
            field=models.PositiveIntegerField(default=0, editable=False, blank=True),
        ),
    ]
