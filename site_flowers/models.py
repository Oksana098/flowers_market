from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

CHOICES = (
    ('0', 'Roze'),
    ('1', 'Tulip')
)

CHOICES_LOGIC = (
    ('0', 'Yes'),
    ('1', 'No')
)


class Flowers(models.Model):
    flowers_name = models.CharField(max_length=255, unique=True)
    color_flowers = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField()
    date_created = models.DateField()
    code = models.CharField(max_length=50, unique=True)
    type_flowers = models.CharField(max_length=50, choices=CHOICES)
    discount = models.CharField(max_length=3, choices=CHOICES_LOGIC)

    class Meta:
        verbose_name = 'Flower'
        verbose_name_plural = 'Flowers'

    def __unicode__(self):
        return '{}'.format(self.flowers_name)


class FlowersPrice(models.Model):
    flowers = models.ForeignKey(Flowers, related_name='retail_price')
    price = models.FloatField()

    def __unicode__(self):
        return '{}'.format(self.flowers)


class DistributorPrice(models.Model):
    flowers = models.ForeignKey(Flowers, related_name='distributor_price')
    price = models.FloatField()

    class Meta:
        verbose_name = 'Distributor Price'
        verbose_name_plural = 'Distributor Prices'

    def __unicode__(self):
        return '{}'.format(self.flowers)


class Order(models.Model):
    # TODO default to date_created
    date_created = models.DateField(null=True, blank=True, default=timezone.now)
    date_order = models.DateField('Time Delivery')
    name = models.CharField('Name', max_length=20)
    phone = models.CharField('Phone', max_length=15)
    email = models.EmailField('Email', max_length=40)
    count = models.PositiveIntegerField('Count Flowers')
    delivery = models.CharField(max_length=3, choices=CHOICES_LOGIC)
    delivery_address = models.CharField(max_length=100)
    flowers = models.ForeignKey(Flowers, related_name='order')

    def __unicode__(self):
        return '{}'.format(self.name)

    @property
    def discount(self):
        discount = 10
        if self.flowers.discount == '1':
            try:
                retail_price = self.flowers.retail_price.filter()[0].price * self.count
                distributor_price = self.flowers.distributor_price.filter()[0].price * self.count
            except Exception as e:
                return 0

            if retail_price - distributor_price > 400:
                return distributor_price / 100 * discount

            return 0

        return 0
