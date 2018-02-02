from __future__ import unicode_literals

from django.db import models

CHOICES = (
    ('1', 'Roze'),
    ('2', 'Tulip')
)

CHOICES_LOGIC = (
    ('1', 'Yes'),
    ('2', 'No')
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
    date_created = models.DateField()
    count = models.IntegerField()
    flowers = models.ForeignKey(Flowers, related_name='order')
    delivery = models.CharField(max_length=3, choices=(('1', 'Yes'), ('2', 'No')))
    street = models.CharField(max_length=255)

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
