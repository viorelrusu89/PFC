# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'finalapp.views.home', name='home'),
	url(r'^ncommits', 'finalapp.views.ncommits', name='ncommits'),
	url(r'^timeseries', 'finalapp.views.timeseries', name='timeseries'),
    # Examples:
    # url(r'^$', 'mypfc.views.home', name='home'),
    # url(r'^mypfc/', include('mypfc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)