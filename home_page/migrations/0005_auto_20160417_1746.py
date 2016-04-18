# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0004_auto_20160417_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='categoriesDisplay',
            field=models.CharField(default='IN', max_length=2, choices=[('IN', 'India'), ('WO', 'World'), ('SP', 'Sports')]),
        ),
    ]
