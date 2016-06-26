from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.post, name='post'),
    url(r'^posts/$', views.posts, name='posts'),
]
