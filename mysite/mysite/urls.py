from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from pwr_1 import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#                       url(r'^polls/',include('polls.urls')),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', views.index),
#    url(r'^$', include(admin.site.urls)),
    url(r'index/$', views.index),
    url(r'^$',views.register_page),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$',logout),
    url(r'syncdb_test_items/$', views.sync_test_items),
    
)
