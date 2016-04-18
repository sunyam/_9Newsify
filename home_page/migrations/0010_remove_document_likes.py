# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0009_document_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='likes',
        ),
    ]
