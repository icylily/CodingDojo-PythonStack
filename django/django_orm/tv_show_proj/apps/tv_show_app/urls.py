from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^shows$', views.shows),
    url(r'^shows/new$',views.add_show),
    url(r'^shows/(?P<show_id>\d+)$', views.show_detail),
    url(r'^process$',views.process),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.destroy),
]
