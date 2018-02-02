from django.conf.urls import url

from site_flowers.views import FlowersDetailsView,\
    DistributorPriceDetailsView,\
    FlowersPriceDetailsView,\
    OrderDetailsView,\
    dashboard,\
    flowers_list,\
    order_list, \
    flowers_list_price,\
    distributor_list


urlpatterns = [
    url(r'^flowers/(?P<pk>\d+)/$', FlowersDetailsView.as_view(), name='flower-details'),
    url(r'^price/(?P<pk>\d+)/$', FlowersPriceDetailsView.as_view(), name='flowers-price-details'),
    url(r'^distributor/(?P<pk>\d+)/$', DistributorPriceDetailsView.as_view(), name='distributor-price-details'),
    url(r'^order/(?P<pk>\d+)/$', OrderDetailsView.as_view(), name='order-details'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^flowers-list/$', flowers_list, name='flowers-list'),  # user for url '-' instead of '_'
    url(r'^order-list/$', order_list, name='order-list'),
    url(r'^flowers-list_price/$', flowers_list_price, name='flowers-list-price'),
    url(r'^distributor-list/$', distributor_list, name='distributor-list'),

]
