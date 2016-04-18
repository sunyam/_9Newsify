from django.contrib import admin
from home_page.models import *
from updown.models import *


# Register your models here.

admin.site.register(Document)
admin.site.register(Vote)