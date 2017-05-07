# -*- coding: utf-8 -*-
__author__ = "Tiago Vizoto"
__email__ = "vizoto123@gmail.com"

from django.conf.urls import url
from . import views
from django.conf.urls import include


urlpatterns = [
    url(r'^jobs/$', views.JobListPublic.as_view()),
    url(r'^jobs/(?P<pk>[0-9]+)/$', views.JobDetailPublic.as_view()),
    url(r'^rh/jobs/$', views.JobList.as_view()),
    url(r'^rh/jobs/(?P<pk>[0-9]+)/$', views.JobDetail.as_view()),
    url(r'^rh/candidaty/$', views.CandidatyList.as_view()),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]