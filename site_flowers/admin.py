from django.contrib import admin
from .models import Flowers, FlowersPrice, DistributorPrice, Order


class FlowersDashboard(admin.ModelAdmin):
    list_display = ('flowers_name', 'color_flowers')
    search_fields = ('flowers_name', 'color_flowers')


class OrderDashboard(admin.ModelAdmin):
    list_display = ('flowers', 'discount')


admin.site.register(Flowers, FlowersDashboard)
admin.site.register(FlowersPrice)
admin.site.register(DistributorPrice)
admin.site.register(Order, OrderDashboard)

