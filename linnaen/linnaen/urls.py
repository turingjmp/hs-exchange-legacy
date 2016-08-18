from django.conf.urls import patterns, include, url

import linnaen.views

urlpatterns = patterns('',

    url(r'^family$', linnaen.views.genus_list),
    url(r'^genus$', linnaen.views.genus_list),
    url(r'^species$', linnaen.views.species_list),
    url(r'^species/(.+)', linnaen.views.species)
)
