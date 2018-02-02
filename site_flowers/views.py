from django.views.generic.detail import DetailView
from site_flowers.models import Flowers, FlowersPrice, DistributorPrice, Order
from django.shortcuts import render


class FlowersDetailsView(DetailView):
    model = Flowers
    template_name = 'flowers.html'


class FlowersPriceDetailsView(DetailView):
    model = FlowersPrice
    template_name = 'flowers_price.html'


class DistributorPriceDetailsView(DetailView):
    model = DistributorPrice
    template_name = 'distributor_price.html',


class OrderDetailsView(DetailView):
    model = Order
    template_name = 'order.html'


def dashboard(request):
    object = Flowers.objects.all()
    return render(request, 'dashboard.html', {'object': object})


def flowers_list(request):
    # wtf with names of variables?
    # why in all views you get from flowers model?

    object = Flowers.objects.all()
    return render(request, 'flowers_list.html', {'object': object})


def flowers_list_price(request):
    # wtf
    object = FlowersPrice.objects.all()
    return render(request, 'flowers_list_price.html', {'object': object})


def order_list(request):
    # wtf
    object = Order.objects.all()
    return render(request, 'order_list.html', {'object': object})


def distributor_list(request):
    # shit
    object = Flowers.objects.all()
    return render(request, 'distributor_list.html', {'object': object})




