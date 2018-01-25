from django.contrib import admin
from .models import Flowers, FlowersPrice


class FlowersDashboard(admin.ModelAdmin):
    list_display = ('flowers_name', 'color_flowers', 'type')
    search_fields = ('flowers_name', 'color_flowers', 'type')


admin.site.register(Flowers, FlowersDashboard)
admin.site.register(FlowersPrice)

