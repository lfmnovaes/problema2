from django.conf.urls import patterns, url
#from django.contrib import admin

from vuln import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^vuln_view/(?P<pk>\d+)$', views.vuln_view, name='vuln_view'),
    url(r'^vuln_new$', views.vuln_create, name='vuln_new'),
    url(r'^vuln_edit/(?P<pk>\d+)$', views.vuln_update, name='vuln_edit'),
    url(r'^vuln_delete/(?P<pk>\d+)$', views.vuln_delete, name='vuln_delete'),
]