from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^itemsList/(?P<id>\d+)/$', views.items_list, name='items_list'),
]
