from __future__ import unicode_literals

from django.db import models
import secretballot


# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    title = models.CharField(max_length=100)


secretballot.enable_voting_on(Document)