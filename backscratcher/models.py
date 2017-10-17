from django.db import models
from django.contrib.postgres.fields import ArrayField


class Backscratcher(models.Model):
    SIZE_CHOICES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )

    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_size = ArrayField(
        models.CharField(choices=SIZE_CHOICES, max_length=2, default='M')
    )
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('item_name',)
