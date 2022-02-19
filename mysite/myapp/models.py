import email
from django.db import models

class add_item(models.Model):
    item = models.CharField(max_length=100)
    price = models.CharField(max_length=100000000)
    barcode = models.CharField(max_length=10)
    link = models.CharField(max_length=2000)

    def __str__(self):
        return self.item
