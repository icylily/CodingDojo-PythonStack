### random_word ###

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]
