from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.urls import reverse

from site_flowers.forms.order import OrderForm
from site_flowers.models import Flowers, FlowersPrice, DistributorPrice, Order


class FlowersDetailsView(DetailView):
    model = Flowers
    template_name = 'flowers.html'


class FlowersPriceDetailsView(DetailView):
    model = FlowersPrice
    template_name = 'flowers_price.html'


class DistributorPriceDetailsView(DetailView):
    model = DistributorPrice
    template_name = 'distributor_price.html'


class OrderDetailsView(DetailView):
    model = Order
    template_name = 'order.html'


def dashboard(request):
    dashboard_list = Flowers.objects.all()
    return render(request, 'dashboard.html', {'dashboard_list': dashboard_list})


def flowers_list(request):
    flowers = Flowers.objects.all()
    return render(request, 'flowers_list.html', {'flowers': flowers})


def flowers_list_price(request):
    flowers_price = FlowersPrice.objects.all()
    return render(request, 'flowers_list_price.html', {'flowers_price': flowers_price})


def order_list(request):
    order = Order.objects.all()
    return render(request, 'order_list.html', {'order': order})


def distributor_list(request):
    distributor_price = DistributorPrice.objects.all()
    return render(request, 'distributor_list.html', {'distributor_price': distributor_price})


def order_flowers(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('order-details', kwargs={'pk': form.instance.pk}))
    else:
        form = OrderForm()
    return render(request, 'order_flowers.html', {'form': form})




