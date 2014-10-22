from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                           ListView.as_view(
                                            query=Poll.objects.order_by('-pub_date')[:5],
                                            context_object_name='latest_poll_list',
                                            template_name='polls/index.heml')),
                       url(r'^(?P<pk>\d+)/$',
                            DetailView.as_view(
                                               model=Poll,
                                               template_name='polls/detail.html')),
                       url(r'^(?P<pk>\d+)/results/$',
                           DetailView.as_view(
                                              model=Poll,
                                              template_name='polls/results.html'),
                                              name='poll_results'),
                       url(r'^(?P<poll_id>\d+)/vote/$','polls.views.vote'),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    url(r'^admin/', include(admin.site.urls)),
)
