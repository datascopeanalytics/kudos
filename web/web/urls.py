""" Default urlconf for web """

from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    url(r'', include('base.urls')),
)
