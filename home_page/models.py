from __future__ import unicode_literals

from django.db import models
#import secretballot

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    title = models.CharField(max_length=100)

    #for categories
    INDIA = 'IN'
    WORLD = 'WO'
    SPORTS = 'SP'
    


    categoryChoices = (
    	(INDIA, 'India'),
    	(WORLD, 'World'),
    	(SPORTS, 'Sports'),

    	)

    categories = models.CharField(max_length=2, 
    									choices=categoryChoices,
    									default='None')
    #likers = models.ManyToManyField(UserProfile,blank=True)
    

