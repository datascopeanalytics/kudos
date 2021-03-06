"""urlconf for the base application"""

from django.conf.urls import url, patterns, include

from . import views

urlpatterns = patterns('',
    url(r'^$', views.KudoCreate.as_view(), name='kudo_create'),
    url(r'^kudos-given/$', views.KudosGiven.as_view(), name='kudos_given'),
    url(r'^kudos-received/$', views.KudosReceived.as_view(), name='kudos_received'),
)
