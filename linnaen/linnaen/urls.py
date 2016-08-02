from django.conf.urls import patterns, include, url

import linnaen.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linnaen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^species/', linnaen.views.listSpecies),
    url(r'^species/.+/', linnaen.views.getSpecies)
)
