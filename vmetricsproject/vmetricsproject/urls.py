from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'vmetricsproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^ncommits', 'vmetricsapp.views.ncommits', name='ncommits'),
    url(r'^admin/', include(admin.site.urls)),
)
