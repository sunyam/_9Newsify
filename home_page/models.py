from __future__ import unicode_literals
from registration.signals import user_registered
from django.db import models
from django.dispatch import receiver

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    title = models.CharField(max_length=100)

    #for categories
    INDIA = 'IN'
    WORLD = 'WO'
    SPORTS = 'SP'
    MISCELLANEOUS = 'MI'


    categoryChoices = (
    	(INDIA, 'India'),
    	(WORLD, 'World'),
    	(SPORTS, 'Sports'),
        (MISCELLANEOUS, 'Miscellaneous'),

    	)

    categories = models.CharField(max_length=2, choices=categoryChoices, default='None')
    likes = models.IntegerField(default=0) 
    dislikes = models.IntegerField(default=0)

    voters = models.SlugField(max_length=200,default = "start_")
    

