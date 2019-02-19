###users.urls####
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register,name="my_new"),
    url(r'^login$',views.login),
    url(r'^users/new$', views.new_user),
    url(r'^users$',views.all_users)
    # url(r'^create$', views.create),
    # url(r'^(?P<number>\d+)$', views.show),
    # url(r'^(?P<number>\d+)/edit$', views.edit),
    # url(r'^(?P<number>\d+)/delete$', views.destory)
]
