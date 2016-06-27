from django.conf.urls import url
from auto_py import views as py_views

urlpatterns = [
    url(r'^$',py_views.register,name="index"),
    url(r'^md5/$',py_views.md5,name="md5"),
    ]
