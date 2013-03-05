from django.conf.urls import patterns, url

from flatpage.models import Page

urlpatterns = patterns('',
    url(r'^(?P<url>\w+)/$', 'flatpage.views.index', name='page'),
)
