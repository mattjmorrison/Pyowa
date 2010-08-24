from django.conf.urls.defaults import *
from Pyowa.microblog import views


urlpatterns = patterns('microblog',
    url(r'^$', views.index, name='list'),
    url(r'^add/$', views.add, name="add"),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name="edit"),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name="delete"),

)