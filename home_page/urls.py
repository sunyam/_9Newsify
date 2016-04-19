from django.conf.urls import url
from . import views

urlpatterns = [
        url('^$', views.home, name='home'),
        url('^india', views.cat_india, name='cat_india'),
        url('^world', views.cat_world, name='cat_world'),
        url('^sports', views.cat_sports, name='cat_sports'),
        url('^misc', views.cat_misc, name='cat_misc'),
        url('^specials', views.specials, name='specials'),
        url(r'^upvote/(?P<photo_id>[0-9]+)/$', views.upvote, name='upvote'),
        url(r'^downvote/(?P<photo_id>[0-9]+)/$', views.downvote, name='downvote'),
    ]
