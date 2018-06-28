from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^itemsList/(?P<id>\d+)/$', views.get_items_list, name='items_list'),
    url(r'^itemsList/add/$', views.add_items_list, name='add_items_list'),
    url(r'^itemsList/(?P<id>\d+)/edit/$', views.edit_items_list, name='edit_items_list'),
    url(r'^itemsList/(?P<id>\d+)/delete/$', views.delete_items_list, name='delete_items_list'),
    url(r'^itemsList/(?P<list_id>\d+)/item/(?P<id>\d+)/$', views.get_item, name='item'),
    url(r'^itemsList/(?P<list_id>\d+)/item/add/$', views.add_item, name='add_item'),
    url(r'^itemsList/(?P<list_id>\d+)/item/(?P<id>\d+)/edit/$', views.edit_item, name='edit_item'),
    url(r'^itemsList/(?P<list_id>\d+)/item/(?P<id>\d+)/delete/$', views.delete_item, name='delete_item'),
    url(r'^itemsList/(?P<list_id>\d+)/item/(?P<id>\d+)/buy/$', views.buy_item, name='buy_item'),
]
