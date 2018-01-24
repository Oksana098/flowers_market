from __future__ import unicode_literals

from django.db import models


class Flowers(models.Model):
    flowers_title = models.CharField(max_length=300)
    color_flowers = models.CharField(max_length=200)
    description_flowers = models.TextField()


class FlowersPrice(models.Model):
    flowers = models.ForeignKey(Flowers)
    flowers_price = models.IntegerField()
    discount = models.IntegerField()


