from sqlite3.dbapi2 import Timestamp

from django.db import models

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Client(TimeStampModel):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
class Product(TimeStampModel):
    qualtiy_choices = (
    ("basic","Basic"),
    ("premium","Premium"),
    )
    quality = models.CharField(choices=qualtiy_choices, max_length=10)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField(null=True, blank=True)
class Check(TimeStampModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buy_time = models.DateTimeField(auto_now_add=True)
shoxruh = "lox"