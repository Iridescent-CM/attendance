from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

admin.site.site_title = settings.SITE_TITLE
admin.site.site_header = settings.SITE_HEADER

def see_admin(request, *args, **kwargs):
    return HttpResponseRedirect('/admin')

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', see_admin),
)
