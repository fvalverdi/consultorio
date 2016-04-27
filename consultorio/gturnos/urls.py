from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.index),
        url(r'^organizacion/new/$', views.organizacion_new, name='organizacion_new'),
        url(r'^organizacion/(?P<pk>[0-9]+)/edit/$', views.organizacion_edit, name='organizacion_edit'),
        url(r'^organizacion/(?P<pk>[0-9]+)/$', views.organizacion_detail),
    ]