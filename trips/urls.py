from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trips import views

urlpatterns = [

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^overviews/$', views.OverviewList.as_view()),
    url(r'^overviews/(?P<pk>[0-9]+)/$', views.OverviewList.as_view()),
    url(r'^segments/$', views.SegmentList.as_view()),
    url(r'^segments/(?P<pk>[0-9]+)/$', views.SegmentDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

