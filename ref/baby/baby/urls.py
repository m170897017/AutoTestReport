from django.conf.urls import patterns, include, url
from baby.views import hello
#from accounts import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('accounts.views',
    # Examples:
    # url(r'^$', 'baby.views.home', name='home'),
    # url(r'^baby/', include('baby.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^hello1/$', 'hello1'),
    url(r'^search/$', 'search'),
)
# you can add another para after function as a func para
# for example, url(r'test/', 'test', {'para':para})
urlpatterns += patterns('baby.views',
                        url(r'^$', 'hello'),
                        )

