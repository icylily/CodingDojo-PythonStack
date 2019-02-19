from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$',views.process),
    url(r'^books/(?P<number>\d+)$', views.show_book),
    url(r'^authors$',views.authors),
    url(r'^authors/(?P<number>\d+)$', views.show_author),
]
