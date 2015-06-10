from django.conf.urls import patterns, include, url
#from books.views import hours_ahead, current_datetime, base_view
from books import views as v
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newtest.views.home', name='home'),
    # url(r'^newtest/', include('newtest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),    
#    (r'^$','newtest.helloworld.index'),
#    (r'^add/$','newtest.add.index'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/(\d+)/$', v.hours_ahead),
    url(r'^time/$', v.current_datetime),
    url(r'^$', v.base_view),
    url(r'^search_form/$',v.search_form),
    url(r'^search/$',v.search),
    url(r'^contact/$',v.contact),
    
)
