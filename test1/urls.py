from django.conf.urls import url
from test1 import views as test1_views

urlpatterns = [
    url(r'^$',test1_views.index,name="index"),
    #url(r'^(?P<test1_id>\d+)/$',test1_views.vote,name='vote'),
    url(r'^post/(?P<test1_id>\d+)/$',test1_views.post_ready,name='post_ready'),
    #url(r'^1/rep',test1_views.post_ok,name='post_ok'),
    url(r'^post/(?P<test1_id>\d+)/rep/$',test1_views.post_ok,name='post_ok'),

    url(r'^get/(?P<test1_id>\d+)/$',test1_views.get_ready,name='get_ready'),
    url(r'^get/(?P<test1_id>\d+)/rep/$',test1_views.get_ok,name='get_ok'),
    ]