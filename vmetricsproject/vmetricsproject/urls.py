from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'vmetricsapp.views.home', name='home'),
	url(r'^ncommits', 'vmetricsapp.views.ncommits', name='ncommits'),
	url(r'^timeseries', 'vmetricsapp.views.timeseries', name='timeseries'),
    url(r'^admin/', include(admin.site.urls)),
)