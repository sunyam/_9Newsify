from django.conf.urls import url
from . import views

urlpatterns = [
        url('^$', views.home, name='home'),
        url('^login', views.login, name='login'),
        # url(r'^list/$', views.list, name='list'),
    ]
