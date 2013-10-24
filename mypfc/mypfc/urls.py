from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'mypfc.views.home', name='home'),

	#TODO: poner 3 funciones
	#1. /users ¿and projects? 2. /"user"/projects 3. /"user"/commits

	url(r'^users', mypfc.views.users),
	url(r'^projects/(.*)', mypfc.views.projects),
	url(r'^commits/(.*)', mypfc.views.commits),
    # Examples:
    # url(r'^$', 'mypfc.views.home', name='home'),
    # url(r'^mypfc/', include('mypfc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
