from django.conf.urls.defaults import *
from Pyowa.microblog import views


urlpatterns = patterns('microblog',
    url(r'^/?$', views.index, name="index"),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name="edit"),
)