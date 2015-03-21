"""urlconf for the base application"""

from django.conf.urls import url, patterns, include

from . import views

urlpatterns = patterns('',

    (r'^accounts/', include('allauth.urls')),

    url(r'^$', views.KudoCreate.as_view(), name='kudo_create'),
    url(r'^kudos/(?P<id>\d+)$', views.KudoUpdate.as_view(), name='kudo_update'),
)
