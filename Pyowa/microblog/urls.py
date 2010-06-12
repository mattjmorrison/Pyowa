from django.conf.urls.defaults import *
from Pyowa.microblog import views


urlpatterns = patterns('microblog',
    (r'^/?$', views.index),

)