from __future__ import unicode_literals

from django.db import models

CHOICES = (
    ('1', 'Roze'),
    ('2', 'Tulip')
)


class Flowers(models.Model):
    flowers_name = models.CharField(max_length=255, unique=True)
    color_flowers = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField()
    date = models.DateField()
    code = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50, choices=CHOICES)

    class Meta:
        verbose_name = 'Flower'
        verbose_name_plural = 'Flowers'

    def __unicode__(self):
        return '{}'.format(self.flowers_name)


class FlowersPrice(models.Model):
    flowers = models.ForeignKey(Flowers)
    flowers_price = models.IntegerField()
    discount = models.IntegerField()

    class Meta:
        verbose_name = 'FlowerPrice'
        verbose_name_plural = 'Flowers Prices'

    def __unicode__(self):
        return '{}'.format(self.flowers_price)
