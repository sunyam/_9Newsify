from django.conf.urls import url
from . import views

urlpatterns = [
        url('^$', views.home, name='home'),
        url('^india', views.cat_india, name='cat_india'),
        url('^world', views.cat_world, name='cat_world'),
        url('^sports', views.cat_sports, name='cat_sports'),
    ]
