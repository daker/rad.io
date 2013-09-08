from django.conf.urls.defaults import *

urlpatterns = patterns("www.radio.views",
    url(r'^category/$', 'categories', name='categories'),
    url(r'^category/(?P<id>\d+)/$', 'category', name='category'),

    url(r'^continent/$', 'continent', name='continent'),
    url(r'^continent/(?P<id>\d+)/$', 'country', name='country'),
    url(r'^country/(?P<id>\d+)/$', 'countrystations', name='countrystations'),

    url(r'^language/$', 'languages', name='languages'),
    url(r'^language/(?P<id>\d+)/$', 'language', name='language'),

    url(r'^network/$', 'networks', name='networks'),
    url(r'^network/(?P<id>\d+)/$', 'network', name='network'),

    url(r'^station/(?P<id>\d+)/$', 'station', name='station'),

    url(r'^nearby/$', 'nearby', name='nearby'),
    url(r'^search/$', 'search', name='search'),

)