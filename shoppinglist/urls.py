from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^itemsList/(?P<id>\d+)/$', views.get_items_list, name='items_list'),
    url(r'^item/(?P<id>\d+)/$', views.get_item, name='item'),
    url(r'^itemsList/add/$', views.add_items_list, name='add_items_list'),
    url(r'^itemsList/(?P<id>\d+)/edit/$', views.edit_items_list, name='edit_items_list'),
]
