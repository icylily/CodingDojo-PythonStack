from django.conf.urls import url, include
from . import views
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'process/post_message$',views.process_post_message),
    url(r'process/post_comment$', views.process_post_comment),
    # url(r"^process/register$", views.process_register),
    # url(r'^process/login$', views.process_login),
    # url(r'^success$', views.success),
    # url(r'^logout$', views.logout)
]
