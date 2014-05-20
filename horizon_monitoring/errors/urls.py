
from django.conf.urls import *
from .views import IndexView, CreateView, UpdateView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^error/(?P<id>[\w\.\-]+)/update/$', UpdateView.as_view(), name='update'),
    url(r'^error/(?P<id>[\w\.\-]+)/create/$', CreateView.as_view(), name='create'),
)
