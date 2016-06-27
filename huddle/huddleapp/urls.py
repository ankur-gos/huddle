from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/$', views.post, name='post'),
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^(?P<post_id>[0-9]+)/post/$', views.postDetail, name='postDetail'),
    url(r'^followup/$', views.followup, name='followup'),
    url(r'^followupComment/$', views.followupComment, name='followupComment'),
    url(r'^studentEdit/$', views.addStudentEdit, name='addStudentEdit'),
]
