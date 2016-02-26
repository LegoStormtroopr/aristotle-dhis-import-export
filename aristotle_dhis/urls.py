from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('aristotle_ddi_utils.views',
#These are required for about pages to work. Include them, or custom items will die!
#    url(r'^about/(?P<template>.+)/?$', views.DynamicTemplateView.as_view(), name="about"),
    url(r'^/?$', TemplateView.as_view(template_name='aristotle_dhis/about_dhis.html'), name="about"),
    url(r'^about/?$', TemplateView.as_view(template_name='aristotle_dhis/about_dhis .html'), name="about"),
)