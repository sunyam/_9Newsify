# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0006_auto_20160417_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='document',
            name='categories',
            field=models.CharField(default='None', max_length=2, choices=[('IN', 'India'), ('WO', 'World'), ('SP', 'Sports'), ('MI', 'Miscellaneous')]),
        ),
    ]
