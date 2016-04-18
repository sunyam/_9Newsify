# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0005_auto_20160417_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='categoriesDisplay',
        ),
        migrations.AddField(
            model_name='document',
            name='categories',
            field=models.CharField(default='None', max_length=2, choices=[('IN', 'India'), ('WO', 'World'), ('SP', 'Sports')]),
        ),
    ]
